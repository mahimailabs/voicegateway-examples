# INDEX

Catalog of release-paired examples in this repo. Every folder under 'examples/' has exactly one row in this table, and every row links to a real folder. Adding a new example means adding a new row.

## Examples

| Slug | Title | Summary | voicegateway release | Folder |
| --- | --- | --- | --- | --- |
| 01-hello-voicegateway | Hello, voicegateway | Smallest end-to-end voicegateway agent. Speaks a greeting and prints a cost-by-modality summary at the end of the call. | v0.0.5 | [examples/01-hello-voicegateway/](./examples/01-hello-voicegateway/) |

## How to add a new row

When a new 'voicegateway' release ships and you add an example for it:

1. Copy 'templates/voicegateway-base/' to 'examples/NN-kebab-case-slug/' and follow that template's README to fork it.
2. Append one row to the table above. Set the release column to the exact 'voicegateway' release the example is paired to.
3. Keep the folder link relative ('./examples/...') and confirm the folder exists. Orphan rows or missing rows are catalog inconsistencies and will be flagged by the consistency check described in [CLAUDE.md](./CLAUDE.md).

## See also

- [README.md](./README.md): repo-wide overview, including how this repo differs from 'awesome-voice-apps'.
- [CLAUDE.md](./CLAUDE.md): conventions for naming, packaging, scope, tone, and the Refinery / Foundry / Ralph pipeline.
- 'templates/voicegateway-base/': the canonical starter for any new example.
