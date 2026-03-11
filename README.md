# AML Mid-Sem Examination Submission

**Name:** Ayush Gupta  
**Roll Number:** 230092  
**Institute:** NST, Rishihood University, Sonipat  
**Course:** Advanced Machine Learning  

---

## Project Overview

This repository contains the submission for the Advanced Machine Learning Mid-Semester Examination. The primary focus is **Part B**, which involves the reproduction and analysis of the paper:

> **"Suboptimal Solution Path Algorithm for Support Vector Machine"**  
> *M. Karasuyama and I. Takeuchi, ICML, 2011.*

The project reproduces the core contribution of the paper—a suboptimal path algorithm that prunes redundant breakpoints in the SVM regularization path using a user-specified tolerance level.

## Repository Structure

The project is organized into two main parts:

### Part A: General Concepts & LLM Usage
- `llm_usage_partA.json`: Disclosure for LLM usage in Part A.

### Part B: Paper Reproduction & Analysis
- **`notebooks/`**: Contains Jupyter notebooks for each task:
  - `task_1_x.ipynb`: Understanding and background research.
  - `task_2_x.ipynb`: Implementation and reproduction of the baseline and suboptimal path.
  - `task_3_x.ipynb`: Ablation studies and failure mode analysis.
- **`disclosures/`**: JSON files capturing LLM usage for each task according to the specified format.
- **`requirements.txt`**: List of dependencies (e.g., `fpdf2`, `numpy`, `scikit-learn`).
- **`data/` & `results/`**: Directories for dataset storage and experimental output.

## Technical Highlights

- **Effective Pruning:** Successfully reproduced a 70% reduction in regularization path segments with minimal impact on decision boundary accuracy.
- **Ablation Studies:** Verified that epsilon-relaxation is the primary driver of computational efficiency.
- **Efficiency:** Demonstrated that multi-point updates are essential for escaping degenerate states at breakpoints.

## How to Run

1. **Install Dependencies:**
   ```bash
   pip install -r partB/requirements.txt
   ```
2. **Explore Notebooks:**
   Run the Jupyter notebooks in `partB/` sequentially to see the reproduction process and analysis.

---
*Submission Date: 12th March 2026*
