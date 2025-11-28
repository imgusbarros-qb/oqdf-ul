\# OQDF-UL Technical Specification  

\### Open Quantum Data Format — Unlimited Layers  

\*\*Version:\*\* 1.0  

\*\*Author:\*\* Agustín Rodrigues De Barros  

\*\*License:\*\* Apache 2.0



---



\## 1. Introduction



OQDF-UL is a hardware-neutral, high-level quantum data format designed to encode classical datasets into quantum-ready representations.  

It defines \*\*what quantum state or transformation is intended\*\*, while allowing compilers to determine \*\*how to realize it\*\* on specific hardware.



The format avoids any dependence on gate sets, qubit topologies, or simulator backends.



OQDF-UL sits above OpenQASM and QIR in the software stack:





---



\## 2. Philosophical Goals



1\. \*\*Unlimited scalability\*\*  

&nbsp;  Qubit count is derived from classical dataset size.



2\. \*\*Abstraction-first\*\*  

&nbsp;  Describes state structure, not gate sequences.



3\. \*\*Hybrid-centric\*\*  

&nbsp;  Ideal for classical pre-processing + quantum execution.



4\. \*\*Interoperability\*\*  

&nbsp;  Compatible with Qiskit, Cirq, PennyLane, Braket, IonQ, and Rigetti.



---



\## 3. Core Components of the Format



\### 3.1 Metadata  

Defines dataset identity, licensing, authorship, tags, and timestamps.



\### 3.2 Classical Source  

Specifies the dataset to be encoded.



\### 3.3 Quantum Space  

Represents:



\- number of qubits  

\- Hilbert dimension  

\- normalization strategy  

\- number of layers (amplitude/phase planes)



\### 3.4 Feature Mapping  

Each classical feature is mapped to one of:



\- `amplitude`  

\- `phase`  

\- `categorical\_phase`  

\- `layered`  

\- `custom` (user-defined transforms)



Mappings may specify:



\- ranges  

\- scale factors  

\- phase rules  

\- categorical encodings  

\- multi-layer parameters  



\### 3.5 Operations  

Describes the workflow to generate the final quantum state:



\- state preparation  

\- layer attachment  

\- transform application  

\- custom rules  



---



\## 4. Validation



OQDF-UL uses a JSON Schema to ensure:



\- structural integrity  

\- valid fields and dimensions  

\- correct encoding types  

\- normalized parameters  



Compilers MUST validate files before execution.



---



\## 5. Compatibility Layer



Adapters may:



\- Compile amplitude-phase layers into state preparation circuits  

\- Map categorical phases to rotation gates  

\- Translate operations into QASM or QIR  

\- Generate variational templates for VQE/QAOA  



This ensures hardware neutrality.



---



\## 6. Versioning



\### v1.0 (this document)

\- JSON-based definition  

\- Unbounded dimensionality  

\- Multi-layer amplitude-phase encoding  

\- Standard operations  

\- Schema for validation  



\### v2.0 (planned)

\- IR adapters (OpenQASM/QIR autogeneration)  

\- Layered compilation models  

\- Plugin system  

\- Binary variant for high-volume datasets  



---



\## 7. Example OQDF-UL File



```json

{

&nbsp; "version": "1.0",

&nbsp; "metadata": {

&nbsp;   "author": "Agustín Rodrigues De Barros",

&nbsp;   "created": "2025-11-08",

&nbsp;   "dataset\_name": "truck\_routes",

&nbsp;   "description": "Quantum-ready routing dataset.",

&nbsp;   "tags": \["optimization", "logistics"]

&nbsp; },

&nbsp; "classical\_source": "routes.csv",

&nbsp; "quantum\_space": {

&nbsp;   "num\_qubits": 4,

&nbsp;   "dimensions": 16,

&nbsp;   "normalization": "L2",

&nbsp;   "layers": 2

&nbsp; },

&nbsp; "feature\_map": \[

&nbsp;   { "name": "miles", "encoding": "amplitude", "range": \[0, 1200], "scale\_factor": 0.51 },

&nbsp;   { "name": "truck\_type", "encoding": "categorical\_phase", "mapping": { "small": 0, "medium": 1.2, "heavy": 2.4 } }

&nbsp; ],

&nbsp; "operations": \[

&nbsp;   { "type": "prepare\_state", "target": "ψ0" },

&nbsp;   { "type": "attach\_layer", "parameters": { "layer": 1 } }

&nbsp; ]

}





