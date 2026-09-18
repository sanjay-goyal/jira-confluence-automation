# Creating Instructions

- Add each new workflow instruction in `./instructions/` as a file named `[name].agent.md`.
- Use a verb-first, hyphen-separated name such as `create-status-report.agent.md`.
- Keep each instruction focused on one workflow or responsibility.
- Use bullet points only; avoid large explanatory sections and long paragraphs.
- Keep sentences short, direct, and actionable.
- Write in English unless the project explicitly requires another language.
- Describe the workflow as clear operational steps, not abstract theory.
- Keep instructions platform-agnostic and IDE-independent.
- Reference shared instructions using `./instructions/[shared-name].agent.md` when relevant.
- Add the new instruction to `./instructions/main.agent.md` with a one-line description.
- Include optional `+ Keywords`, `+ Target`, and `+ Exceptions` sub-bullets when useful.
- Use a structure like:
  + `- [./instructions/example.agent.md](./example.agent.md) — one-line description.`
  + `+ Keywords: word1, word2`
  + `+ Target: src/**/*.ts`
  + `+ Exceptions: avoid when ...`
- When updating an existing instruction, read it first and extend it without rewriting the whole file.
- Preserve useful statements and add new findings incrementally.
- Keep instructions concise enough to be reused without context overload.
- Prefer reusable, composable instructions over one giant monolithic file.
- If a workflow is large, split it into smaller instruction files and compose them from the main catalog.
- Re-check the instruction against real work before treating it as final.
- Treat `main.agent.md` as the entry catalog for the instruction set.
- For VS Code + GitHub Copilot, ensure `.github/copilot-instructions.md` loads `./instructions/main.agent.md` on every prompt.
- Keep the instruction catalog and IDE wrappers aligned with the same source of truth.
- Use real examples only when they are short and practical.
- Prefer clarity and consistency over clever wording.
