# File: even_sum-py
import numpy as np

def sum_even_numbers(numbers):
    """
    Returns the sum of all even numbers in a given list or array.
    Inputs: list or array
    Outputs: sum
    """
    sum = np.sum(num for num in numbers if num%2 == 0)
    return sum