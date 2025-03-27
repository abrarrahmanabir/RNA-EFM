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
## 🔧 Environment Setup

All external dependencies are listed in \`environment.yml\`. To set up the conda environment:

```bash
conda env create -f environment.yml
conda activate rnaefm
```

Additionally, install the following libraries manually (with CUDA compatibility if needed):

```bash
pip install torch-scatter torch-cluster openmm
```

---

##  Running Inference

Once the environment is set up and dependencies are installed, you can run inference to generate RNA sequences and structures conditioned on protein backbones:

```bash
python scripts/inference.py 
```

RNA-EFM will automatically preprocess the input, generate interpolated backbones, and output the designed RNA structures and sequences.

---

## Training Instructions

To train RNA-EFM from scratch:

1. **Download RF2NA Weights**  
   Download the pre-trained RF2NA weights from:

   https://files.ipd.uw.edu/dimaio/RF2NA_apr23.tgz

2. **Place the checkpoint** at:

   `RoseTTAFold2NA/network/weights/RF2NA_apr23.pt`

3. **Start Training**  
   Run the following command:

```bash
python scripts/train.py
```


---



