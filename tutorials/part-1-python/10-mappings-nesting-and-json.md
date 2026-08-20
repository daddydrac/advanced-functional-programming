# 10 — Mappings, Nested Data, and JSON

## Goal

Read, transform, copy, nest, and serialize mappings while keeping the domain model immutable.

Python dictionaries map unique hashable keys to values. API JSON arrives as nested dictionaries and arrays. Pydantic validates it, then LambdaFlux converts it to frozen domain objects.

```python
def with_key(source: dict[str, int], key: str, value: int) -> dict[str, int]:
    return source | {key: value}
```

The union operator creates a new mapping. For nested updates, copying each level is noisy; lesson 39 introduces lenses.

JSON supports objects, arrays, strings, numbers, booleans, and null. It does not preserve Python tuples, enums, datetimes, or arbitrary classes without an encoding rule. Repositories therefore use explicit `*_to_payload` and `payload_to_*` functions.

Serialization is an isomorphism only when both directions preserve information:

$$\operatorname{decode}(\operatorname{encode}(x)) = x$$

## Lab

Inspect the skeletons `candidate_to_payload` and `payload_to_candidate`. List the enum, tuple, evidence, and nested-property conversions, then write the round-trip test before implementing them in chapter 47.

## Checkpoint

Create a JSON-safe encoder/decoder pair for `Calibration`. Test the round-trip law.

Reference coverage: dictionaries, access/change/add/remove concepts, traversal through higher-order functions, copying, nested dictionaries, dictionary methods, and JSON.

## Acceptance criteria

- the small codec satisfies `decode(encode(x)) == x`.
- missing and extra fields are rejected explicitly.
- the future candidate round-trip test is written before chapter 47 implementation.
