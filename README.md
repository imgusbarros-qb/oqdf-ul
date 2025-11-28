<p align="center">
  <img src="https://raw.githubusercontent.com/imgusbarros-qb/oqdf-ul/main/docs/banner.png" width="650" />
</p>

# OQDF-UL  
### **Open Quantum Data Format — Unlimited Layers**

**Version:** 1.0.0  
**License:** Apache 2.0  
**Status:** Public Standard — Initial Release  

OQDF-UL is a hardware-neutral, quantum-ready data format that defines how classical datasets can be represented, structured, and prepared for quantum algorithms using amplitudes, phases, and multilayer encoding.

It acts as an **input abstraction layer**, sitting *above* OpenQASM and QIR, enabling quantum pipelines to receive complex datasets in a structured, portable, scalable format.

This repository contains:
- the official specification (`spec/`)
- schema validation (`schema/`)
- examples (`examples/`)
- tools (`tools/`)
- release materials (`docs/`)
- encoder stub demonstrating usage  


# oqdf-ul
Open Quantum Data Format — Unlimited Layers (OQDF-UL). A hardware-neutral quantum data abstraction standard.

***Open Quantum Data Format — Unlimited Layers


OQDF-UL is an open, hardware-neutral quantum data format designed to represent classical datasets as structured, scalable, quantum-ready abstractions.

It defines what quantum state or transformation is intended, not how it must be implemented on quantum hardware.

OQDF-UL complements existing standards such as OpenQASM 3 and QIR, acting as a higher-level data interface layer in hybrid quantum pipelines.


***Why OQDF-UL?

Existing quantum standards describe circuits, not data

Encodings vary across tools (Qiskit, Cirq, Braket, PennyLane)

No open format exists for storing quantum-ready datasets

Future quantum memory needs a standardized format

Hybrid workflows benefit from a declarative input layer

***OQDF-UL fills this gap with:

Unlimited qubit scaling
Multi-layer amplitude/phase model
JSON-based, human-readable
Validated with JSON Schema
Fully interoperable with QASM/QIR
Future-proof for quantum RAM and photonic storage

***Repository Structure

oqdf-ul/
  schema/
    OQDF-UL.schema.json

  spec/
    OQDF-UL-spec.md

  examples/
    OQDF-UL-example.json
    example_dataset.csv

  docs/
    WHITEPAPER.md
    WHITEPAPER.pdf (generated after release)

  tools/
    oqdf_ul_encoder_stub.py

LICENSE
NOTICE
README.md
CONTRIBUTING.md
CHANGELOG.md
PUBLISHING-GUIDE.md


***Quick Start
1. Install dependencies
pip install jsonschema pandas

2. Run the encoder stub
python tools/oqdf_ul_encoder_stub.py

3. You will get:

schema validation

inferred qubit count

Hilbert dimension

feature encoding summary

quantum blueprint overview


***What Is OQDF-UL Used For?

Hybrid quantum–classical pipelines

Quantum machine learning

Variational algorithms

Job-shop, routing, and optimization models

Future quantum-native storage

Transfer layer between classical ETL and quantum IRs

Data interchange across quantum libraries


***Standard Compliance

OQDF-UL files must validate against: schema/OQDF-UL.schema.json

***All implementations and tools MUST support:

amplitude encodings

phase encodings

categorical phases

unlimited layers

classical/quantum separation

***Roadmap
v1.1

Additional layered encodings

Compression suggestions

v2.0

Compiler adapter interface

OQDF-UL → QASM/QIR autogeneration

Binary format (OQDF-UL-B)

Quantum storage container format (QSCF)

***License

Licensed under Apache License 2.0.
Trademark rights remain with the author.

***Author

Agustín Rodrigues De Barros
Creator and developer of OQDF-UL.

If you find this useful Please star the repository — it helps the project gain visibility in the quantum computing community.
