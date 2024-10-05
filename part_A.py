
from math import sqrt

# using loops
def loops(x):
    N = len(x)
    mean = sum(x) / N 
    sum_of_sq = 0
    for num in x:
        sum_of_sq = sum_of_sq + num ** 2
    mean_of_sq = sum_of_sq / N
    variance = mean_of_sq - mean ** 2

    return sqrt(variance)

# using builtin function
def builtin(x):
    N = len(x)
    mean = sum(x) / N
    mean_of_sq = sum([num ** 2 for num in x]) / N
    variance = mean_of_sq - mean ** 2

    return sqrt(variance)

import numpy as np

# using numpy
def numpy(x):
    return np.std(x)

num_list = [1, 2, 3, 4, 5]

print("Standard deviation using loops:", loops(num_list))
print("Standard deviation using built in functions:", builtin(num_list))
print("Standard Deviation using NumPy:", numpy(num_list))
