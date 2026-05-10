# CLAUDE.md, voicegateway-examples operating playbook

This file auto-loads in every Claude Code session at this repo root. Read it before making any change. It is the source of truth for repo-wide conventions. If a convention here conflicts with the Foundry Blueprint, defer to the Blueprint and update this file.

## What this repo is

A curated set of working voice-agent examples paired to specific 'voicegateway' releases. Every example proves that one release of 'voicegateway' (the SDK at github.com/mahimailabs/voicegateway) does what its release notes claim. New examples are added only when a new 'voicegateway' release ships.

## How this repo differs from 'awesome-voice-apps'

'awesome-voice-apps' is a sister repo: a broad gallery of voice-agent ideas spanning many SDKs, models, and patterns. Its bar is breadth and inspiration. This repo, by contrast, has a single SDK as its subject and a much narrower bar:

- Every example must be release-paired to a specific 'voicegateway' version.
- Every example must demonstrate a capability that the paired release added or fixed.
- If an idea fits 'awesome-voice-apps' better than this repo, it goes there.

**The fail-the-test rule.** Before merging any example, check: if you swap 'voicegateway' out for another inference router and the example still passes, the example does not belong in this repo. Move it to 'awesome-voice-apps' and close the PR here.

Do not edit 'awesome-voice-apps' from inside this repo. Different repo, different cadence.

## Pipeline expectation: Refinery, Foundry, Ralph

Every milestone in this repo follows the same pipeline before any code is written:

1. **Refinery** (Linear). User requirements (REQ-VGE-...) and acceptance criteria observable from outside the system.
2. **Foundry Blueprint** (Linear). Architecture, file paths, dependencies, numbered Implementation items, test strategy. Each item maps back to one or more REQ ids.
3. **Ralph Loop** (this repo, '.agents/'). Per-iteration TODO list, append-only journal, one commit per task on a milestone branch.

Before writing code, ask: which Refinery REQ does this serve, and which Foundry Implementation item describes it? If neither answer exists, stop and propose Refinery or Foundry updates instead of writing code.

Refinery and Foundry documents live exclusively in Linear and are never committed to this repo. Do not create local 'docs/refinery/' or 'docs/foundry/' folders. The only repo-side pointers are '.agents/design.md' (a thin URL pointer) and '.agents/prompt.md' (Ralph operating instructions). The whole '.agents/' folder is gitignored.

## Naming rules

- Project tag: 'VGE'. The foundation milestone uses sub-tag 'FOUND' in REQ ids (REQ-VGE-FOUND-001 through REQ-VGE-FOUND-005). Future milestones use their own sub-tag.
- Example folder slug format: '<NN>-<kebab-case-name>'. 'NN' is a zero-padded sequence number reflecting publishing order, not difficulty. Example: '01-hello-voicegateway'.
- Branch format for milestone work: 'feat/<milestone-slug>'. Example: 'feat/m0-foundation'.
- Commit message format inside a Ralph milestone: 'M<N>/T<NN>: <one-line summary>'. One commit per Ralph iteration.

## Packaging rules

- Every example folder is uv-managed. It ships its own 'pyproject.toml' and is run via 'uv sync' followed by 'uv run ...'. Do not introduce 'pip install -r requirements.txt' flows.
- The canonical entry-point filename is 'agent.py'. Every example exposes a 'main' function wired into '[project.scripts]' so that 'uv run <slug>' starts the agent.
- 'voicegateway' is pinned to the latest stable release on PyPI. If that release is not yet on PyPI, install from 'git+https://github.com/mahimailabs/voicegateway.git@main' and document the gap in the example README. Do not pin to '*', 'latest', or any floating ref in committed code.
- Other voice-stack dependencies ('livekit-agents', STT / LLM / TTS providers) are also pinned to known-good versions.
- '.env.example' files document every required environment variable with placeholder values. Real '.env' files are gitignored and must never be committed.

## Scope rules

- Examples are added only as a release-pairing exercise. A new 'voicegateway' release means at most one new example folder, demonstrating what changed in that release.
- Every example README states the paired 'voicegateway' version explicitly. The catalog table in the root 'README.md' lists every pairing.
- Apply the fail-the-test rule (above) before merging any new example.

## Tone rules

These apply to all narrative prose in this repo (READMEs, this file, Ralph artifacts, PR descriptions):

- No em-dashes anywhere in prose. Use colons, periods, parentheses, or commas instead.
- Use single quotes for inline code references in prose: 'agent.py', 'voicegateway', 'uv run'.
- Backticks are fine inside fenced code blocks for actual code samples and shell commands. Do not use backticks mid-sentence in prose. Pick one or the other: prose uses single quotes, code blocks use backticks.
- No marketing voice. State what the repo does and how to use it; do not sell it.

## Where to look first

- Adding a new example for a 'voicegateway' release: copy 'templates/voicegateway-base/' and follow its README.
- Understanding the layout: 'README.md' at the repo root.
- Catalog of every release-paired example: the table in 'README.md' at the repo root.
- Per-milestone work in flight: '.agents/' (gitignored) and the milestone Linear documents.
