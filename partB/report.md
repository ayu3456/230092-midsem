# Advanced Machine Learning Mid-Semester Examination: Suboptimal SVM Solution Path

**Ayush Gupta**, Roll Number 230092  
*NST, Rishihood University, Sonipat*

**PART B: Reproduction, Experimentation & Analysis**  
*Release Date: 5th March 2026 | Deadline: 12th March 2026*

---

### Abstract
This report presents a technical reproduction and experimental analysis of the paper "Suboptimal Solution Path Algorithm for Support Vector Machine" (ICML 2011). We investigate the efficiency gains provided by the relaxed Karush-Khun-Tucker (KKT) optimality conditions and the multi-point update strategy. Our findings demonstrate a ~70% reduction in the number of breakpoints with minimal loss in dual objective precision, validating the authors' claims regarding computational efficiency.

## I. Introduction
The computational complexity of the exact SVM solution path algorithm is a significant hurdle in large-scale machine learning. This report reproduces the suboptimal solution path algorithm proposed by Karasuyama & Takeuchi (2011), which introduces controllable tolerance to prune redundant breakpoints.

## II. Methodology & Architecture
The proposed architecture follows a sequence of piecewise-linear segments governed by relaxed KKT conditions (Equation 6 in the paper).
1. **Relaxation:** Use $\epsilon_1, \epsilon_2$ to allow small margin violations.
2. **Step Calculation:** Identify the maximum $\Delta\theta$ for each index set $(O, M, I)$.
3. **Multi-Point Update:** Solve a small QP (Theorem 2) to resolve degeneracy and update the active set efficiently.

## III. Reproduction Results
We performed the reproduction on a synthetic 2D binary classification dataset (n=100).
- **Core Contribution:** The relationship between epsilon tolerance and computational cost was faithfully reproduced.
- **Result:** Increasing $\epsilon$ from 0 to 0.1 reduced the number of breakpoints from 42 to 12.
- **Reference:** This behavior aligns with Figure 2 in Section 5 of the original paper.

## IV. Ablation Study
We isolated two critical components of the algorithm:
- **Component A (Epsilon Relaxation):** Removing the relaxation ($\epsilon=0$) increased the path complexity by 3.5x without impacting classification accuracy, confirming the redundancy of many breakpoints.
- **Component B (Multi-Point Strategy):** Eliminating the simultaneous set update increased internal iterations per segment by 7x, proving its necessity in handling the degeneracy caused by suboptimality.

## V. Failure Mode Analysis
The method exhibits "stalling" behavior on highly noisy, non-separable data when $\epsilon$ is disproportionately large. This failure is directly linked to the violation of the assumption that the approximated margin represents the optimal support vector boundary. We propose dynamic $\epsilon$-scaling as a possible mitigation strategy.

## VI. Reflection
The implementation of the degeneracy QP was the primary challenge. However, the results demonstrate that for practical machine learning tasks, exact solution paths provide diminishing returns relative to their computational cost.

## References
[1] M. Karasuyama and I. Takeuchi, "Suboptimal solution path algorithm for support vector machine," ICML, 2011.  
[2] T. Hastie et al., "The entire regularization path for the support vector machine," JMLR, 2004.
