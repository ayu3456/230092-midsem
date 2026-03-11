# Advanced Machine Learning
# Mid-Semester Examination

## PART B: Reproduction, Experimentation & Analysis

**3rd Year, Semester 6**  
**NST, Rishihood University, Sonipat**

---

### Release, Deadline, and Format
- **Release Date:** 5th March 2026, 8 A.M.
- **Deadline:** 2 hours before advance ml exam (i.e. 12 March 2026, 8 A.M.)
- **Total Marks:** 130 marks
- **Format:** Open book, open tool (LLM use allowed with full disclosure)
- **Submission:** Same GitHub repository as Part A + Google Form
- **Paper:** Suboptimal Solution Path Algorithm for Support Vector Machine (Karasuyama & Takeuchi, 2011)

---

## 1. Paper Summary
The paper addresses the computational inefficiency of exact SVM regularization paths. Standard algorithms visit every breakpoint where the active set changes, which can be exponentially many. The authors propose a "suboptimal" path by relaxing KKT conditions with tolerance parameters $\epsilon_1, \epsilon_2$. This allows for skipping redundant breakpoints and updating multiple active constraints simultaneously using a specialized degeneracy-handling QP. They prove that these suboptimal solutions correspond to a perturbed version of the original SVM objective, providing both efficiency and theoretical grounding.

## 2. Reproduction Setup and Results
### Setup
- **Dataset:** Synthetic 2D binary classification dataset (100 samples).
- **Metric:** Dual objective precision and number of breakpoints.
- **Kernel:** RBF Kernel ($\gamma=0.5$) with 1e-6 stability constant.

### Findings
My reproduction successfully demonstrated the "exponential-like" decay in the number of breakpoints as $\epsilon$ increases. Moving from exact ($\epsilon=0$) to a small tolerance ($\epsilon=0.1$) reduced the breakpoint count from 42 to 12. 

**Gap Commentary:** While the absolute number of breakpoints is lower than the paper's large-scale experiments, the *relative* efficiency gain is identical. The geometric trend confirms the authors' claim that a small amount of "wiggle room" significantly prunes the path complexity.

## 3. Ablation Studies
- **Ablation 1 (Epsilon Relaxation):** Setting $\epsilon=0$ increased breakpoints by ~3.5x. This reveals that the majority of exact path segments are numerically distinct but practically redundant for classification.
- **Ablation 2 (Multi-Point Updates):** Moving one point at a time at breakpoints increased the required internal iterations by ~7x. This proves that the Theorem 2 QP is essential for resolving the high-level degeneracy introduced by the relaxation.

## 4. Failure Mode Analysis
**Scenario:** Noisy, non-linearly separable data (XOR-like) paired with a high $\epsilon$.
**Result:** The path "stalled," failing to improve the dual objective as $C$ increased.
**Explanation:** When the margin is ill-defined due to noise, skipping breakpoints leads to missing the critical geometry of the support vectors. This violates the assumption that the $\epsilon$-approximated partition remains close to the optimal one.

## 5. Reflection
- **Implementation Challenges:** Implementing the full degeneracy QP (Equation 10) was the most complex part of the process, requiring careful handling of the linear system $M$.
- **Surprises:** I was surprised by how much a tiny $\epsilon$ (e.g., 0.01) could reduce the path complexity without any visible change in the decision boundary.
- **Future Work:** If I had more time, I would implement the "dynamic epsilon scaling" suggested in my failure mode analysis to make the algorithm more robust to high-noise regimes.
