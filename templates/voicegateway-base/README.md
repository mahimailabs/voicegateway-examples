# voicegateway-base

The canonical starter for any new release-paired example in this repo. Copy this folder, rename a small fixed set of identifiers, and edit the marked swap points in 'agent.py'. That is the entire workflow.

## What this folder is

A minimal, working voicegateway-instrumented LiveKit Agent. Three files do the real work, plus this README:

- 'agent.py'. The agent. Five numbered swap points ('### SWAP 1' through '### SWAP 5') mark every place an example will customize.
- 'pyproject.toml'. uv-managed dependencies. Pins 'voicegateway' (currently to git+main, see note below), 'livekit-agents' to the 1.x range, and 'python-dotenv'. Defines a 'voicegateway-base' script entry that runs 'agent:main'.
- '.env.example'. Placeholders for every required environment variable. Real '.env' is gitignored.

## How to use it: five steps

### 1. Copy the folder

From the repo root:

```bash
cp -r templates/voicegateway-base examples/NN-your-slug
cd examples/NN-your-slug
```

Replace 'NN' with a zero-padded sequence number reflecting publishing order (look at the highest existing folder under 'examples/' and add one). Replace 'your-slug' with a short kebab-case name describing what the example demonstrates.

### 2. Rename the project identifiers

Edit 'pyproject.toml' and change two lines:

```toml
[project]
name = "NN-your-slug"           # was "voicegateway-base"

[project.scripts]
NN-your-slug = "agent:main"     # was: voicegateway-base = "agent:main"
```

These are the only renames in this file. Everything else (dependencies, build-system, hatch config) stays as is.

### 3. Edit the swap points in 'agent.py'

Open 'agent.py' and edit each marked swap point so it demonstrates one capability of the 'voicegateway' release you are pairing the example to. The points are:

- 'SWAP 1', system prompt. Rewrite 'INSTRUCTIONS' for the example's persona and goal.
- 'SWAP 2', greeting. Rewrite 'GREETING' for the example's opening line.
- 'SWAP 3', model strings. Override 'STT_MODEL', 'LLM_MODEL', or 'TTS_VOICE' defaults if the release adds support for a specific model.
- 'SWAP 4', STT, LLM, TTS factories. Switch providers or add tools, function calls, or guardrails here.
- 'SWAP 5', opening turn. Replace 'session.generate_reply' with a richer flow if the example warrants it.

Optionally rename the 'BaseAgent' class to something descriptive ('HelloAgent', 'PricingAgent', etc.).

### 4. Update '.env.example' and rewrite 'README.md'

If the example introduces new environment variables, add them to '.env.example' with placeholder values and a one-line comment. Do not remove the five required keys.

Replace this README with one focused on the example:

- One-line description of what the example demonstrates.
- The paired 'voicegateway' release (e.g. v0.0.5).
- The five-minute setup path (clone, '.env', 'uv sync', 'uv run').
- A "what you'll see when it works" section.
- A link back to the root 'README.md' and 'INDEX.md'.

### 5. Add a row to 'INDEX.md'

In the catalog table at the repo root, append one row: example slug, title, one-line summary, paired 'voicegateway' release, and a link to the folder. Every folder under 'examples/' must have a row in 'INDEX.md', and every row must link to a real folder.

## What success looks like

Running 'uv sync' followed by 'uv run voicegateway-base' (or 'uv run NN-your-slug' once you have renamed the script) prints standard livekit-agents worker startup logs and, on the first call into the dev room, the agent speaks the greeting line through your TTS provider. If you can hear the greeting, the wiring is correct.

## Note on the 'voicegateway' pin

While 'voicegateway' v0.0.5 is published only to GitHub, the dependency installs from 'git+https://github.com/mahimailabs/voicegateway.git@main'. Once v0.0.5 lands on PyPI, swap the active line in 'pyproject.toml' for the commented PyPI pin:

```toml
# Before (current):
"voicegateway @ git+https://github.com/mahimailabs/voicegateway.git@main",
# "voicegateway==0.0.5",

# After:
# "voicegateway @ git+https://github.com/mahimailabs/voicegateway.git@main",
"voicegateway==0.0.5",
```

Then re-run 'uv sync'. No other code changes needed.

## Conventions

This folder honors the repo-wide conventions in [../../CLAUDE.md](../../CLAUDE.md): uv-managed packaging, 'agent.py' as the canonical entry point, the example-folder slug format 'NN-kebab-case', and the no-em-dashes / single-quotes-for-inline-code prose style.
