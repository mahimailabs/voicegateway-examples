# voicegateway-examples

Working voice-agent examples paired to specific releases of [voicegateway](https://github.com/mahimailabs/voicegateway). Every example here proves that one release of the SDK does what its release notes claim. Open one folder, run two commands, hear the agent talk.

## What this is

A small, opinionated catalog. Each entry under 'examples/' is a self-contained, uv-managed Python project that:

- Pins one specific 'voicegateway' release.
- Demonstrates a capability that release added or fixed.
- Runs end-to-end on a clean machine in roughly five minutes.

If you want a broad survey of voice-agent ideas across SDKs, see the sister repo 'awesome-voice-apps'. This repo is narrower on purpose: one SDK, one example per release, every example tied to a feature in that release.

## Who it is for

- Developers evaluating 'voicegateway' who want a runnable proof, not a marketing page.
- Existing 'voicegateway' users tracking what changed in a new release.
- Contributors building demos: copy 'templates/voicegateway-base/' and follow its README.

If you have never written a Python voice agent before, start at 'examples/01-hello-voicegateway/'. The example is intentionally minimal so you can see every wire.

## How this repo differs from 'awesome-voice-apps'

| | this repo | 'awesome-voice-apps' |
| --- | --- | --- |
| Scope | one SDK ('voicegateway') | many SDKs and patterns |
| Bar to merge | release-paired, fail-the-test rule | breadth and inspiration |
| Cadence | one example per 'voicegateway' release | open-ended |
| Catalog | 'INDEX.md' (this repo) | curated list in that repo |

The fail-the-test rule. If you can swap 'voicegateway' out for any other inference router and the example still passes, the example does not belong here. It belongs in 'awesome-voice-apps'.

## Where to start

1. Read [examples/01-hello-voicegateway/](./examples/01-hello-voicegateway/). Five minutes from clone to a talking agent.
2. Browse [INDEX.md](./INDEX.md) for the full catalog of release-paired examples.
3. To add a new example, copy [templates/voicegateway-base/](./templates/voicegateway-base/) and follow its README.

## Repo layout

```text
voicegateway-examples/
├── CLAUDE.md                      Operating playbook for AI agents and contributors.
├── INDEX.md                       Catalog: example slug → paired voicegateway release.
├── LICENSE                        MIT.
├── README.md                      You are here.
├── .claude/                       Claude Code project config (committed).
│   ├── agents/
│   ├── skills/
│   └── slash-commands/
├── templates/
│   └── voicegateway-base/         Canonical starter. Copy to begin a new example.
│       ├── agent.py
│       ├── pyproject.toml
│       ├── .env.example
│       └── README.md
└── examples/
    └── 01-hello-voicegateway/     Start here. Paired to voicegateway v0.0.5.
        ├── agent.py
        ├── pyproject.toml
        ├── .env.example
        └── README.md
```

## License

MIT. See [LICENSE](./LICENSE).
