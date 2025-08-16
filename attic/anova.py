import numpy as np
from scipy.stats import f_oneway

# Generate sample data for three independent groups
# Assume these represent scores from three different teaching methods
group1_scores = np.array([85, 88, 79, 92, 87, 90, 81, 75, 83, 89])
group2_scores = np.array([78, 81, 75, 88, 82, 79, 70, 85, 76, 80])
group3_scores = np.array([91, 94, 85, 98, 93, 96, 88, 82, 90, 95])

# Perform the one-way ANOVA test
f_statistic, p_value = f_oneway(group1_scores, group2_scores, group3_scores)

# Print the results
print(f"F-statistic: {f_statistic:.2f}")
print(f"P-value: {p_value:.4f}")

# Interpret the results
alpha = 0.05  # Significance level
if p_value < alpha:
    print("Reject the null hypothesis: There is a significant difference between at least one pair of group means.")
else:
    print("Fail to reject the null hypothesis: There is no significant difference between the group means.")