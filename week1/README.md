# Week 1 – Neural Signal Feature Engineering

# Central Question
How can we efficiently extract meaningful features from neural activity over time?

# Algorithms Used
- Arrays
- Prefix sums
- Sliding window
- Dynamic programming (basic)

## Methods
I model neural firing rates as time-series data. Using sliding windows, I extract
local temporal features. Prefix sums are used to optimize cumulative computations.
Dynamic programming is applied to segment the signal into optimal intervals.

## Key Result
Efficient feature extraction reveals temporal structure in neural activity while
reducing computational cost.

## Limitations
- Synthetic data only
- No noise modeling yet

## Next Step
Apply the same pipeline to real neural recordings and compare robustness.
