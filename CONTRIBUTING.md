# Contributing to OQDF-UL  
Thank you for your interest in contributing to the **Open Quantum Data Format — Unlimited Layers (OQDF-UL)** project.

OQDF-UL is an open standard licensed under **Apache License 2.0**, and contributions are welcome from researchers, developers, engineers, and the broader quantum community.

---

## Types of Contributions Welcome
- Improvements to the specification  
- Schema refinements  
- Encoder and decoder implementations  
- Compiler adapters (QASM3, QIR, Cirq, Qiskit, PennyLane)  
- Documentation improvements  
- Test datasets  
- Bug reports and issue discussions  

---

##  How to Contribute

### 1. Fork the repository

https://github.com/imgusbarros-qb/oqdf-ul


### 2. Create a feature branch
git checkout -b feature/my-improvement


### 3. Follow the coding guidelines
- Keep code clean and commented  
- Keep schema changes backward-compatible whenever possible  
- When proposing changes to the standard, open an issue first  
- Use JSON Schema Draft 2020-12 for validation  

### 4. Commit with clear messages

git commit -m "Added support for TransformBlocks in OQDF-UL schema"


### 5. Push and open a Pull Request  
Include:
- a clear explanation of the goal  
- any breaking changes  
- examples or test data (if applicable)  

---

## Testing Guidelines
If contributing code (tools/adapters):
- Include minimal reproducible examples  
- Ensure JSON validates against the schema  
- Provide at least one example OQDF-UL file  

---

## 📄 Licensing Requirements
By contributing, you agree that your contributions fall under the  
**Apache 2.0 License of the project**.

If a contribution introduces external dependencies, they **must** be compatible with Apache 2.0.

---

## Community Agreement
All contributors must follow respectful communication.  
Technical criticism is welcome; personal criticism is not.

---

Thanks again for helping shape the future of open quantum data standards!
