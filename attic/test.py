import numpy as np
from scipy import stats

# Sample data for two independent groups
group_A = np.array([180, 172, 168, 190, 175])
group_B = np.array([170, 165, 160, 180, 172])

# Perform two-sample independent t-test (assuming equal variances)
t_statistic, p_value = stats.ttest_ind(group_A, group_B, equal_var=True)

print(f"\nTwo-Sample Independent T-Test:")
print(f"T-statistic: {t_statistic:.4f}")
print(f"P-value: {p_value:.4f}")