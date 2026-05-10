# voicegateway-examples

Working voice agents you can run in five minutes, each paired to a real release of [voicegateway](https://github.com/mahimailabs/voicegateway).

Every folder under 'examples/' is a self-contained, uv-managed Python project that wires up real STT, LLM, and TTS providers through 'voicegateway', demonstrates one capability of a specific release, and runs end-to-end on a clean machine. Pick a release, open the matching folder, run two commands, hear the agent talk.

## Catalog

| Example | What it demonstrates | Paired release |
| --- | --- | --- |
| [01-hello-voicegateway](./examples/01-hello-voicegateway/) | Hello-world voice agent that prints a per-modality cost summary at the end of each call. | v0.0.5 |

A new release of 'voicegateway' means at most one new row in this table.

## Quick start

```bash
git clone https://github.com/mahimailabs/voicegateway-examples.git
cd voicegateway-examples/examples/01-hello-voicegateway
cp .env.example .env       # then fill DEEPGRAM_API_KEY, OPENAI_API_KEY,
                           # CARTESIA_API_KEY, VOICEGATEWAY_URL, VOICEGATEWAY_TOKEN
uv sync
uv run agent.py dev
```

Connect from any LiveKit client and talk to the agent. When the call ends, the terminal prints the cost-by-modality summary for the call. Full prerequisites, success signals, and troubleshooting are in the example's own [README](./examples/01-hello-voicegateway/).


## Adding a new example

When a new 'voicegateway' release ships:

1. Copy [templates/voicegateway-base/](./templates/voicegateway-base/) to 'examples/NN-kebab-case-slug/' and follow that template's README.
2. Edit the marked swap points in 'agent.py' to demonstrate the new release's capability.
3. Append one row to the Catalog table above: slug, what it demonstrates, paired release.

The full conventions (naming, packaging, scope, tone, the Refinery / Foundry / Ralph pipeline) live in [CLAUDE.md](./CLAUDE.md).

## License

MIT. See [LICENSE](./LICENSE).
