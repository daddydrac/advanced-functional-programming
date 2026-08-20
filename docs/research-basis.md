# Research Basis and Tutorial Translation

This document records why each scientific feature appears in the workshop and where the tutorial deliberately simplifies reality.

## 1. Reactor material roles

The U.S. Department of Energy identifies plasma-facing components, structural fusion materials, blanket materials, and enabling materials as major fusion-material areas. LambdaFlux represents the first three as `ReactorRole`; it does not imply that one property set is valid for every component.

Source: [DOE Fusion Energy Sciences FY 2025 request](https://www.energy.gov/sites/default/files/2024-03/FY2025-PresidentsRequest-FES.pdf).

## 2. Heat and plasma-facing constraints

ITER describes heat and particle exhaust at the divertor as a primary engineering challenge and has moved its first-wall armour direction from beryllium to tungsten. This motivates melting point, thermal conductivity, expansion, elastic properties, and a plasma-facing role in the tutorial.

Sources: [ITER: Making fusion work](https://www.iter.org/fusion-energy/making-it-work), [ITER blanket system](https://www.iter.org/machine/blanket).

## 3. Neutrons, damage, and activation

D-T fusion produces neutrons near 14 MeV. Those neutrons support energy production and tritium breeding while also causing activation and material damage. LambdaFlux carries normalized neutron-tolerance and activation fields only as synthetic proxies; real values depend on spectrum, fluence, temperature, microstructure, and time.

Sources: [IAEA MoD-PMI contributions](https://conferences.iaea.org/event/403/contributions/), [DOE Fusion Energy Sciences FY 2024 request](https://www.energy.gov/media/291458).

## 4. Refractory alloys and competing objectives

Recent work investigates tungsten-containing refractory alloys and reports tradeoffs among high-temperature behavior, ductility, printability, and radiation response. A 2026 computational/experimental study explicitly examined a melting-point/Pugh-ratio Pareto front for W-Ta-Nb alloys. That makes Pareto dominance a scientifically meaningful way to teach partial orders without collapsing all evidence into one hidden score.

Sources: [W-Ta-Nb computational design preprint](https://arxiv.org/abs/2601.11295), [MoNbTaVW radiation-tolerance study](https://arxiv.org/abs/2411.02834), [W-Ta-V irradiation study](https://arxiv.org/abs/2406.15022).

## 5. Data interoperability

OPTIMADE defines a common REST API for querying multiple materials databases, while the Materials Project provides a supported API and curated Matbench datasets. Chapter 54 treats an OPTIMADE/Materials Project adapter as an extension because crystal/thermodynamic properties alone do not supply qualified fusion-neutron performance.

Sources: [OPTIMADE specification](https://www.optimade.org/specification/latest/), [Materials Project API](https://docs.materialsproject.org/downloading-data/using-the-api), [Matbench](https://github.com/materialsproject/matbench).

## 6. AI and active experimentation

Materials research uses active learning to balance promising predictions with informative experiments. LambdaFlux starts with the transparent acquisition proxy $a(x)=u(x)+\beta\sigma(x)$, then asks local Ollama only to turn deterministic evidence into a proposed experiment plan. The LLM does not calculate the Pareto front and cannot qualify a material.

Sources: [Bayesian optimization benchmark for materials experiments](https://www.nature.com/articles/s41524-021-00656-9), [Ames Laboratory DuctGPT project](https://www.ameslab.gov/news/ductgpt-demonstrates-how-ai-can-accelerate-discovery-of-next-generation-fusion-materials).

## Safety boundary

All bundled numeric values are fictional. The formulas are learning proxies. A real program requires qualified source data, exposure conditions, validated multiphysics models, uncertainty propagation, domain review, and experimental confirmation.
