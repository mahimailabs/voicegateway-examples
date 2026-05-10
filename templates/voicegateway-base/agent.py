"""Canonical voicegateway-instrumented LiveKit Agent template.

Copy this folder to start a new example. The structure deliberately follows
the LiveKit Agents AgentSession pattern, with provider factories obtained
through 'voicegateway.inference' so STT, LLM, and TTS calls are routed
through your VoiceGateway deployment for unified billing and observability.

Swap points are marked '### SWAP <N>:' below. Each derived example edits one
or more swap points to demonstrate a specific 'voicegateway' release feature.
Keep this file the smallest possible end-to-end working agent. Anything
example-specific belongs in the example folder, not here.
"""

from __future__ import annotations

import os

from dotenv import load_dotenv
from livekit.agents import Agent, AgentSession, JobContext, WorkerOptions, cli
from voicegateway import inference

# Load '.env' from the same folder as this file. Only '.env.example' is
# committed; real secrets must never enter git.
load_dotenv()


# ### SWAP 1: System prompt.
# Each example replaces these instructions to shape the agent's persona,
# task, and tone. Keep it short here so the diff in each example stays small.
INSTRUCTIONS = (
    "You are a friendly voice assistant built on voicegateway. "
    "Greet the caller, answer briefly, and end calls cleanly when asked."
)


# ### SWAP 2: Greeting.
# Spoken once when the call starts. Examples may replace this with a richer
# opening, a tool call, or a personalized hello.
GREETING = "Hello, this is the voicegateway base template. How can I help?"


# ### SWAP 3: Provider model strings.
# Sourced from environment variables so the same agent can be re-targeted
# without code edits. The 'voicegateway' factory takes a single model string
# in the 'provider/model' format (for example 'deepgram/nova-3'); the
# provider prefix selects the underlying livekit-plugins backend. Defaults
# match the '.env.example' shipped alongside.
STT_MODEL = os.environ.get("STT_MODEL", "deepgram/nova-3")
LLM_MODEL = os.environ.get("LLM_MODEL", "openai/gpt-4o-mini")
TTS_MODEL = os.environ.get("TTS_MODEL", "cartesia/sonic-3")
TTS_VOICE = os.environ.get("TTS_VOICE", "f786b574-daa5-4673-aa0c-cbe3e8534c02")


class BaseAgent(Agent):
    """Minimal Agent. Replace 'INSTRUCTIONS' (SWAP 1) to customize behavior."""

    def __init__(self) -> None:
        super().__init__(instructions=INSTRUCTIONS)


async def entrypoint(ctx: JobContext) -> None:
    """LiveKit Agents entry point. Connects to the room, starts the session,
    speaks the greeting, then yields control to the framework which handles
    teardown when the room closes.
    """
    await ctx.connect()

    # ### SWAP 4: STT, LLM, TTS factories.
    # 'inference.STT/LLM/TTS' are generic factories. Each resolves the
    # provider (the prefix before '/' in the model string), looks up its
    # API key from the active 'voicegw' project, and returns a drop-in
    # livekit-plugins instance wrapped for cost and latency tracking.
    # To switch providers, change the prefix in the matching env var
    # (see SWAP 3). API keys are managed via 'voicegw onboard'.
    session = AgentSession(
        stt=inference.STT(model=STT_MODEL),
        llm=inference.LLM(model=LLM_MODEL),
        tts=inference.TTS(model=TTS_MODEL, voice=TTS_VOICE),
    )

    await session.start(room=ctx.room, agent=BaseAgent())

    # ### SWAP 5: Opening turn.
    # Examples may replace 'generate_reply' with a tool call, a 'tts.say',
    # or a richer flow. Keep at least one greeting so the operator hears
    # that the wiring works end-to-end.
    await session.generate_reply(instructions=f"Say exactly: {GREETING}")


def main() -> None:
    """Entry point exposed as 'voicegateway-base' via [project.scripts]."""
    cli.run_app(WorkerOptions(entrypoint_fnc=entrypoint))


if __name__ == "__main__":
    main()
