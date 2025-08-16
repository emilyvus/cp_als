import numpy as np
from scipy.stats import tukey_hsd
import matplotlib.pyplot as plt  # Import for visualization

# Sample data (replace with your actual data)
group0 = [24.5, 23.5, 26.4, 27.1, 29.9]
group1 = [28.4, 34.2, 29.5, 32.2, 30.1]
group2 = [26.1, 28.3, 24.3, 26.2, 27.8]

# Perform Tukey's HSD test
result = tukey_hsd(group0, group1, group2)

# Print the results
print(result)
print ("--------------")
print(result.pvalue)

