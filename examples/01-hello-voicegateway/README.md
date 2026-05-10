# 01-hello-voicegateway

The introductory example for [voicegateway-examples](../../README.md). Paired to 'voicegateway' v0.0.5. Five minutes from clone to a talking agent.

## What this example demonstrates

A minimum-viable voicegateway-instrumented LiveKit Agent with three example-specific behaviors, marked in 'agent.py' with '### EXAMPLE EDIT' comments:

1. A friendlier hello-world system prompt and greeting (EDIT 1).
2. An end-of-call query against the gateway's '/v1/costs' endpoint (EDIT 2).
3. A printed cost-by-modality summary block, broken down across STT, LLM, and TTS (EDIT 3).

## Prerequisites

- Python 3.11 or newer ('voicegateway' requires it).
- 'uv' installed. See https://docs.astral.sh/uv/ for one-line install instructions.
- API keys for Deepgram, OpenAI, and Cartesia (added via 'voicegw onboard' in step 3, not via env).
- A VoiceGateway deployment URL and token. Optional for the first run; the example skips the cost query gracefully if unset.
- A LiveKit dev environment (LiveKit Cloud or a local dev server) so a client can join the agent's room.

## Five-minute setup

1. Clone the repo and enter this folder:

   ```bash
   git clone https://github.com/mahimailabs/voicegateway-examples.git
   cd voicegateway-examples/examples/01-hello-voicegateway
   ```

2. Install dependencies:

   ```bash
   uv sync
   ```

3. One-time 'voicegw' setup. Creates 'voicegw.yaml' with your project, providers, and keys:

   ```bash
   uv run voicegw onboard
   ```

   This five-question wizard records your Deepgram, OpenAI, and Cartesia keys in 'voicegw.yaml' (treated like a credential file; do not commit it). If anything later looks off, run 'uv run voicegw doctor' for a diagnostic punch list.

4. Fill the env file (LiveKit and VoiceGateway deployment values, no provider keys):

   ```bash
   cp .env.example .env
   $EDITOR .env  # fill LIVEKIT_URL, LIVEKIT_API_KEY, LIVEKIT_API_SECRET,
                 # VOICEGATEWAY_URL, VOICEGATEWAY_TOKEN
   ```

5. Run the agent against your LiveKit dev room:

   ```bash
   uv run agent.py dev
   ```

6. Connect from any LiveKit client (CLI, web, or mobile) and start talking.

## What you'll see when it works

On the terminal:

- Standard 'livekit-agents' worker startup logs ("registered worker", room subscription, etc.).
- When a client joins the room, the agent speaks the greeting:

  > "Hi there, and welcome to the voicegateway hello-world demo. Ask me anything about voicegateway, or say goodbye to end the call."

- You can hold a short back-and-forth conversation. Latency should feel natural for hosted STT, LLM, and TTS.
- When the call ends (the client disconnects or you stop the worker), the terminal prints a cost summary:

  ```
  ========================================================
  voicegateway cost summary
  ========================================================
  modality          usd        units unit
  --------------------------------------------------------
  stt           0.0123           42 seconds
  llm           0.0045          812 tokens
  tts           0.0089          210 characters
  --------------------------------------------------------
  total         0.0257
  ========================================================
  ```

If you skipped 'VOICEGATEWAY_URL' or 'VOICEGATEWAY_TOKEN', you will instead see this fallback line, then an empty summary block. That is expected for a first-time setup before VoiceGateway is wired up:

```
[hello-voicegateway] VOICEGATEWAY_URL or VOICEGATEWAY_TOKEN not set; skipping '/v1/costs' query.
```

## Note on the 'voicegateway' pin

While 'voicegateway' v0.0.5 is published only to GitHub, this example installs from 'git+https://github.com/mahimailabs/voicegateway.git@main'. Once v0.0.5 lands on PyPI, swap the active line in 'pyproject.toml' for the commented PyPI pin. The exact one-line swap is documented in [../../templates/voicegateway-base/README.md](../../templates/voicegateway-base/README.md).

## Customize this example

Open 'agent.py' and edit the three '### EXAMPLE EDIT' markers:

- EDIT 1, system prompt and greeting.
- EDIT 2, '/v1/costs' query helper.
- EDIT 3, cost-by-modality summary renderer.

To start a fresh example instead of editing this one, copy [../../templates/voicegateway-base/](../../templates/voicegateway-base/) and follow its README.

## See also

- Root [README.md](../../README.md): repo-wide overview, the catalog of all release-paired examples, and how this repo differs from 'awesome-voice-apps'.
- [CLAUDE.md](../../CLAUDE.md): repo-wide conventions (naming, packaging, scope, tone).
