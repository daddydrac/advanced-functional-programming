# 04 — Numbers, Units, and Fusion-Energy Scales

## Goal

Work safely with integers, floating-point values, scientific notation, casting, units, and mathematical domains using a D-T fusion example.

Python integers have arbitrary precision. Floats implement IEEE 754 binary arithmetic, so decimal values are approximate. Use floats for scientific computation only when units and tolerances are explicit.

## Particle-physics context

A deuterium-tritium reaction releases about $17.6\,\text{MeV}$, with approximately $14.1\,\text{MeV}$ carried by the neutron and $3.5\,\text{MeV}$ by the alpha particle:

$$
{}^2\mathrm{H}+{}^3\mathrm{H}\rightarrow{}^4\mathrm{He}+n.
$$

That neutron energy helps explain why fusion-material response cannot be inferred from ordinary-temperature properties alone.

## Worked example: explicit unit conversion

```python
ELECTRON_VOLT_J = 1.602176634e-19

def mev_to_joules(energy_mev: float) -> float:
    return energy_mev * 1e6 * ELECTRON_VOLT_J
```

The name includes the source unit and the return contract should document joules. A naked `convert(14.1)` would be ambiguous.

## Casting is partial

`float("14.1")` succeeds while `float("fourteen MeV")` fails. Later, `Result` makes this failure part of the type rather than an exception surprise.

Complex numbers use $a+bj$, with magnitude $|z|=\sqrt{a^2+b^2}$. They appear naturally in wave/impedance calculations, but LambdaFlux's starter screening fields are real scalars.

## Lab

Convert $14.1\,\text{MeV}$ and $3.5\,\text{MeV}$ to joules. Verify their sum equals the converted $17.6\,\text{MeV}$ within floating-point tolerance.

## Checkpoint

Write `safe_ratio(numerator, denominator) -> Result[float, str]`. Division by zero and non-finite inputs return `Err` rather than throwing or silently producing unusable evidence.

Reference coverage: numbers, numeric types, scientific notation, casting, built-in math, and the `math`/`cmath` module families.

## Acceptance criteria

- Unit conversions are explicit in names and documentation.
- the energy partition agrees within a justified tolerance.
- zero denominator and non-finite values return `Err`.
- no bundled screening proxy is described as a measured material constant.
