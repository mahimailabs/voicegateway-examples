"""01-hello-voicegateway: the introductory example for voicegateway-examples.

The smallest agent that proves voicegateway is wired correctly. Forked from
'templates/voicegateway-base/agent.py'. After the call ends it queries the
gateway's '/v1/costs' endpoint and prints a modality-by-modality summary so
the operator can see how the call broke down across STT, LLM, and TTS.

Three example-specific edits, flagged with '### EXAMPLE EDIT N:' markers:

  EDIT 1, friendlier hello-world system prompt and greeting.
  EDIT 2, '/v1/costs' query at the end of the call.
  EDIT 3, printed cost-by-modality summary block.

Paired to 'voicegateway' v0.0.5.
"""

from __future__ import annotations

import os
from typing import Any

import httpx
from dotenv import load_dotenv
from livekit.agents import Agent, AgentSession, JobContext, WorkerOptions, cli
from voicegateway import inference

load_dotenv()


# ### EXAMPLE EDIT 1: Friendlier hello-world system prompt and greeting.
# The base template ships a generic assistant persona. This example uses a
# warmer first-time-user opener so newcomers feel oriented before they start
# poking at the swap points.
INSTRUCTIONS = (
    "You are the voicegateway hello-world host. Welcome the caller, briefly "
    "mention that this is a release-paired demo from the voicegateway-examples "
    "repo, and answer questions in two sentences or fewer. Be warm and concise."
)

GREETING = (
    "Hi there, and welcome to the voicegateway hello-world demo. "
    "Ask me anything about voicegateway, or say goodbye to end the call."
)

# Model strings stay env-driven (same as the base template). 'voicegateway'
# expects 'provider/model' format; the prefix selects the backend.
STT_MODEL = os.environ.get("STT_MODEL", "deepgram/nova-3")
LLM_MODEL = os.environ.get("LLM_MODEL", "openai/gpt-4o-mini")
TTS_MODEL = os.environ.get("TTS_MODEL", "cartesia/sonic-3")
TTS_VOICE = os.environ.get("TTS_VOICE", "f786b574-daa5-4673-aa0c-cbe3e8534c02")


class HelloAgent(Agent):
    """Friendly first-call host. Replace 'INSTRUCTIONS' to retarget."""

    def __init__(self) -> None:
        super().__init__(instructions=INSTRUCTIONS)


# ### EXAMPLE EDIT 2: '/v1/costs' query at the end of the call.
async def fetch_call_costs() -> dict[str, Any] | None:
    """GET '<VOICEGATEWAY_URL>/v1/costs' and return the parsed JSON body.

    Returns None if 'VOICEGATEWAY_URL' or 'VOICEGATEWAY_TOKEN' is not set, so
    the example still runs end-to-end before VoiceGateway is fully configured.
    The contributor sees a clear "skipped" message in that case.
    """
    base = os.environ.get("VOICEGATEWAY_URL")
    token = os.environ.get("VOICEGATEWAY_TOKEN")
    if not base or not token:
        print(
            "[hello-voicegateway] VOICEGATEWAY_URL or VOICEGATEWAY_TOKEN not "
            "set; skipping '/v1/costs' query."
        )
        return None

    url = f"{base.rstrip('/')}/v1/costs"
    headers = {"Authorization": f"Bearer {token}"}

    async with httpx.AsyncClient(timeout=10.0) as client:
        try:
            response = await client.get(url, headers=headers)
            response.raise_for_status()
        except httpx.HTTPError as exc:
            print(f"[hello-voicegateway] '/v1/costs' query failed: {exc}")
            return None

    return response.json()


# ### EXAMPLE EDIT 3: Cost-by-modality summary block.
def print_cost_summary(payload: dict[str, Any] | None) -> None:
    """Render a small per-modality cost table from the '/v1/costs' response.

    Expected payload shape:

        {
            "totals": {"usd": <float>},
            "by_modality": {
                "stt": {"usd": <float>, "units": <int>, "unit": "seconds"},
                "llm": {"usd": <float>, "units": <int>, "unit": "tokens"},
                "tts": {"usd": <float>, "units": <int>, "unit": "characters"},
            },
        }

    Missing fields fall back to zero so the block always renders.
    """
    print()
    print("=" * 56)
    print("voicegateway cost summary")
    print("=" * 56)

    if not payload:
        print("No cost data available (gateway unreachable or unconfigured).")
        print("=" * 56)
        return

    totals_usd = (payload.get("totals") or {}).get("usd", 0.0)
    by_modality = payload.get("by_modality") or {}

    print(f"{'modality':<10} {'usd':>10} {'units':>12} {'unit':<12}")
    print("-" * 56)
    for modality in ("stt", "llm", "tts"):
        row = by_modality.get(modality) or {}
        usd = row.get("usd", 0.0)
        units = row.get("units", 0)
        unit_label = row.get("unit", "-")
        print(f"{modality:<10} {usd:>10.4f} {units:>12} {unit_label:<12}")
    print("-" * 56)
    print(f"{'total':<10} {totals_usd:>10.4f}")
    print("=" * 56)


async def entrypoint(ctx: JobContext) -> None:
    """Connect, greet, then on shutdown query '/v1/costs' and print a summary."""
    await ctx.connect()

    async def on_shutdown() -> None:
        costs = await fetch_call_costs()
        print_cost_summary(costs)

    ctx.add_shutdown_callback(on_shutdown)

    session = AgentSession(
        stt=inference.STT(model=STT_MODEL),
        llm=inference.LLM(model=LLM_MODEL),
        tts=inference.TTS(model=TTS_MODEL, voice=TTS_VOICE),
    )

    await session.start(room=ctx.room, agent=HelloAgent())
    await session.generate_reply(instructions=f"Say exactly: {GREETING}")


def main() -> None:
    """Entry point exposed as '01-hello-voicegateway' via [project.scripts]."""
    cli.run_app(WorkerOptions(entrypoint_fnc=entrypoint))


if __name__ == "__main__":
    main()
