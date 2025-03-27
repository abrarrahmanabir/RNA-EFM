# RNA-EFM: Energy Based Flow Matching for Protein-conditioned RNA Sequence-Structure Co-design

## 🧬 Overview

**RNA-EFM** is a deep learning framework for jointly designing RNA sequences and backbone structures conditioned on a target protein. The method integrates **flow matching** for geometric alignment and **biophysically-informed energy refinement** to generate RNA molecules that are both structurally accurate and thermodynamically stable. 

The framework leverages recent advances in geometric deep learning and incorporates biophysical constraints, such as **Lennard-Jones potential** and **sequence-derived free energy**, into an iterative refinement process guided by an **idempotent objective**.

## 🔬 Key Novelties

- **Protein-conditioned RNA co-design**: Joint prediction of RNA sequence and 3D backbone structure based on the input protein complex.
- **Energy-based refinement**: Incorporates physically meaningful constraints (e.g., van der Waals interactions and free energy) during training.
- **Flow Matching Objective**: Supervises geometric alignment between predicted and native RNA structures via interpolation-based learning.
- **Idempotent Refinement**: Predictive consistency is enforced by repeatedly applying the structure predictor until convergence.
- **Biological Relevance**: Designed RNAs exhibit improved thermodynamic stability and better binding affinity with the target protein.

## 🛠️ Installation

```bash
git clone [https://github.com/yourusername/RNA-EFM.git](https://github.com/abrarrahmanabir/RNA-EFM.git)
cd RNA-EFM

```
