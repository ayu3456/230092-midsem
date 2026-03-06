# Dataset Documentation - Part B

## Toy Dataset: Sine vs. Square Waves
The dataset used in Task 2 is synthetically generated within the notebooks using `numpy`. 

### Generation Details
- **Samples**: 150
- **Features**: 50 (time steps)
- **Classes**: 2 (Sine wave, Square wave)
- **Source**: `generate_toy_data()` function in `task 2 1.ipynb`.

### Usage
- `task 2 1.ipynb`: Selection and visualization.
- `task 2 2.ipynb`: Shapelet Transform training.
- `task 3 1.ipynb`: Ablation experiments.

### Limitations
Compared to the UCR Time Series datasets used in the original paper, this dataset:
1. Is significantly smaller and balanced.
2. Has less noise and no warping.
3. Only captures a single discriminative difference (curviness vs. sharp corners).
