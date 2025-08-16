import numpy as np
from scipy.stats import f_oneway

# Sample data for three different groups
group1 = np.array([25, 28, 30, 27, 26])
group2 = np.array([32, 35, 30, 33, 31])
group3 = np.array([20, 22, 19, 21, 23])

# Perform one-way ANOVA
f_statistic, p_value = f_oneway(group1, group2, group3)

print(f"F-Statistic: {f_statistic:.2f}")
print(f"P-Value: {p_value:.4f}")

# Interpret the results
alpha = 0.05
if p_value < alpha:
    print("Reject the null hypothesis: There is a statistically significant difference between the group means.")
else:
    print("Fail to reject the null hypothesis: There is no statistically significant difference between the group means.")