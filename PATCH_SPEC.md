# PATCH SPEC — Atom 2.1 Patch Bundle Contract

This repo accepts changes via a **patch bundle**.

## Requirements
- Output must be **valid JSON** (no trailing commas).
- Must include:
  - `commit_message` (string)
  - `files` (array of objects)
  - each file object has:
    - `path` (string, repo-relative)
    - `content` (string, FULL file contents)
- Do **not** include commentary outside JSON.
- Always include complete file contents (not diffs).

## JSON schema (informal)
```json
{
  "commit_message": "...",
  "files": [
    { "path": "relative/path.ext", "content": "full file text...\n" }
  ]
}
```

## Example: update a YAML value
```json
{
  "commit_message": "Update next_focus",
  "files": [
    {
      "path": "active_state_pointer.yaml",
      "content": "meta:\n  name: ...\n...\n"
    }
  ]
}
```

## Notes
- CI enforces **Atom2.1_superseed.yaml** as source-of-truth via rendering.
- If you change split-pack files, prefer changing **SuperSeed** and re-rendering.
- Apply bundles using:
  - `paste_patch.bat` (recommended)
  - or `python agent_apply.py --stdin`
