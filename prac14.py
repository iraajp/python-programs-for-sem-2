import numpy as np
from scipy.stats import pearsonr

# Function to calculate mean
def calculate_mean(data):
    return np.mean(data)

# Function to calculate median
def calculate_median(data):
    return np.median(data)

# Function to calculate variance
def calculate_variance(data):
    return np.var(data)

# Function to calculate standard deviation
def calculate_standard_deviation(data):
    return np.std(data)

# Function to calculate Pearson correlation coefficient
def calculate_correlation_coefficient(data1, data2):
    correlation, _ = pearsonr(data1, data2)
    return correlation

# Example data array
data1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Calculate mean, median, variance, and standard deviation
mean = calculate_mean(data1)
median = calculate_median(data1)
variance = calculate_variance(data1)
std_deviation = calculate_standard_deviation(data1)

# Print the results
print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Variance: {variance}")
print(f"Standard Deviation: {std_deviation}")

# For correlation coefficient, we need a second array. Let's create data2.
data2 = np.array([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])

# Calculate correlation coefficient
correlation_coefficient = calculate_correlation_coefficient(data1, data2)
print(f"Pearson Correlation Coefficient between data1 and data2: {correlation_coefficient}")
