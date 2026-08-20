# 23 — File Handling in the Imperative Shell

## Goal

Read, write, create, and delete files safely while keeping parsing and transformation pure.

File operations depend on external state, permissions, encoding, and timing. Keep them at the edge:

```python
def parse_lines(text: str) -> Result[tuple[Observation, ...], str]:
    ...

def load_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")
```

`load_text` is effectful; `parse_lines` can be referentially transparent. Use context managers for resources. Specify encoding. Validate resolved paths before exposing file access through an API. Prefer deletion only when the user explicitly requested it and the target is exact.

The tutorial service reads Markdown from a read-only Compose bind mount. PostgreSQL owns durable application data; the API container itself is read-only.

## Lab

Inspect `TutorialService`. Explain how matching a slug against discovered files prevents direct `../` traversal.

## Checkpoint

Create pure `encode_csv` and `decode_csv` functions and a thin file adapter. Test the codec round trip without touching disk.

Reference coverage: file handling, reading, writing/creating, deletion safety, paths, and context managers.

## Acceptance criteria

- codec tests require no filesystem.
- file I/O is a thin adapter around the pure codec.
- destructive path handling is explicit and narrowly scoped.
