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


## 🔧 Environment Setup

All external dependencies are listed in `environment.yml`. To set up the conda environment:

```bash 
conda env create -f environment.yml
conda activate rnaflow
```

In addition, install the following libraries manually (ensuring CUDA compatibility if applicable):

""" + "```bash\n" + """\
pip install torch-scatter torch-cluster openmm
""" + "```\n" + """

---

## 🔄 SE(3)-Transformer Setup

You also need to install NVIDIA's SE(3)-Transformer. **Use the SE3Transformer version included in the repository**:

""" + "```bash\n" + """\
cd RoseTTAFold2NA/SE3Transformer
pip install --no-cache-dir -r requirements.txt
python setup.py install
cd ../../
""" + "```\n" + """

---

## 🚀 Running Inference

Once everything is set up, you can run inference using:

""" + "```bash\n" + """\
python scripts/inference.py
""" + "```\n" + """

---

## 🏋️ Running Training

Make sure to download the RF2NA pre-trained weights from:

https://files.ipd.uw.edu/dimaio/RF2NA_apr23.tgz

Place the downloaded weight file at:

`RoseTTAFold2NA/network/weights/RF2NA_apr23.pt`

Then run the following command to begin training:

""" + "```bash\n" + """\
python scripts/train.py
""" + "```\n" + """

---
"""
