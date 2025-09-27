"""
Core implementation of the Hasse-Stirling framework.

This module provides functions for computing generalized Stirling numbers and
applying the Hasse operator with various parameterizations.
"""

import numpy as np
from functools import lru_cache
from typing import Callable, List, Tuple, Union
import math

@lru_cache(maxsize=10000)
def binomial(n: int, k: int) -> int:
    """Compute binomial coefficient with caching."""
    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1
    if k > n - k:
        k = n - k
    result = 1
    for i in range(k):
        result = result * (n - i) // (i + 1)
    return result

@lru_cache(maxsize=10000)
def generalized_stirling(n: int, k: int, alpha: float = 0, beta: float = 1, r: float = 0) -> float:
    """
    Compute generalized Stirling number S(n,k;alpha,beta,r).
    
    Args:
        n, k: Indices
        alpha, beta, r: Parameters
        
    Returns:
        The generalized Stirling number
    """
    if k > n or k < 0 or n < 0:
        return 0
    
    if n == 0 and k == 0:
        return 1
    
    # Standard Stirling numbers of the second kind
    if alpha == 0 and beta == 1 and r == 0:
        if k == 0:
            return 0 if n > 0 else 1
        if k == n:
            return 1
        if k == 1:
            return 1
        
        return k * generalized_stirling(n-1, k, 0, 1, 0) + generalized_stirling(n-1, k-1, 0, 1, 0)
    
    # General recurrence relation
    return generalized_stirling(n-1, k-1, alpha, beta, r) + (beta*k - alpha*n + r) * generalized_stirling(n-1, k, alpha, beta, r)

def compute_hasse_coefficients(max_m: int, alpha: float = 0, beta: float = 1, r: float = 0) -> List[List[float]]:
    """
    Compute Hasse coefficients H_{m,n}^{alpha,beta,r} up to max_m.
    
    Args:
        max_m: Maximum first index
        alpha, beta, r: Parameters
        
    Returns:
        A list of lists representing the triangular array of coefficients
    """
    # Fix: Initialize with max_m+1 elements in each row to avoid index errors
    H = [[0 for _ in range(max_m+1)] for _ in range(max_m+1)]
    
    H[0][0] = 1
    
    for m in range(1, max_m+1):
        H[m][0] = 1/(m+1)
        for n in range(1, m+1):
            # Use recurrence relation for efficiency
            H[m][n] = H[m-1][n-1] - ((m*alpha + n*beta + r)/(m+2)) * H[m-1][n]
    
    return H

def hasse_operator_action(f: Callable[[float], float], x: float, max_m: int, 
                          alpha: float = 0, beta: float = 1, r: float = 0) -> float:
    """
    Apply the generalized Hasse operator to a function f at point x.
    
    Args:
        f: Function to apply the operator to
        x: Point at which to evaluate
        max_m: Truncation order
        alpha, beta, r: Parameters
        
    Returns:
        Result of applying the Hasse operator
    """
    H = compute_hasse_coefficients(max_m, alpha, beta, r)
    result = 0
    
    for m in range(max_m + 1):
        term = 0
        for n in range(m + 1):
            term += H[m][n] * f(x + n)
        result += term
    
    return result

def hasse_log_power(power: int, x: float, max_m: int, 
                   alpha: float = 0, beta: float = 1, r: float = 0) -> float:
    """
    Apply the generalized Hasse operator to log(t)^power at point x.
    
    Args:
        power: Power of the logarithm
        x: Point at which to evaluate
        max_m: Truncation order
        alpha, beta, r: Parameters
        
    Returns:
        Result of applying the Hasse operator to log(t)^power
    """
    H = compute_hasse_coefficients(max_m, alpha, beta, r)
    result = 0
    
    for n in range(1, max_m + 1):  # Start from 1 to avoid log(0)
        log_term = math.log(x + n)**power
        term_sum = 0
        for m in range(n, max_m + 1):
            term_sum += H[m][n]
        result += term_sum * log_term
    
    return result

def matrix_power_recurrence(recurrence_matrix, initial_values, n):
    """
    Compute the nth term of a recurrence relation using matrix exponentiation.
    
    Args:
        recurrence_matrix: Matrix representing the recurrence relation
        initial_values: Initial values for the recurrence
        n: Target index
        
    Returns:
        The nth term(s) of the recurrence
    """
    if n < len(initial_values):
        return initial_values[n]
    
    # Convert to numpy arrays for matrix operations
    matrix = np.array(recurrence_matrix)
    result = np.array(initial_values)
    
    # Compute matrix^n using binary exponentiation
    n = n - len(initial_values) + 1
    power = matrix
    while n > 0:
        if n % 2 == 1:
            result = power @ result
        power = power @ power
        n //= 2
    
    return result[0]
