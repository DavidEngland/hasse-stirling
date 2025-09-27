"""
Implementation of zeta function values computation using the Hasse-Stirling framework.
"""

import math
from .hasse_stirling import hasse_log_power

def zeta3(precision: float = 1e-15) -> float:
    """
    Compute zeta(3) using the Hasse-Stirling approach.
    
    Args:
        precision: Desired precision
        
    Returns:
        The value of zeta(3)
    """
    # For zeta(3), use parameters (1, -2, 0)
    alpha, beta, r = 1, -2, 0
    max_m = int(-math.log10(precision) * 2) + 10
    
    # The identity H_{1,-2,0}(log(t)^2)(1) = 2*zeta(3) + constants
    h_action = hasse_log_power(2, 1, max_m, alpha, beta, r)
    
    # Extract zeta(3) from the identity
    pi_squared_over_6 = math.pi**2 / 6
    gamma = 0.57721566490153286060651209008240243104215933593992  # Euler's constant
    
    zeta3 = (h_action - gamma**2 - pi_squared_over_6) / 2
    
    return zeta3

def zeta5(precision: float = 1e-15) -> float:
    """
    Compute zeta(5) using the Hasse-Stirling approach.
    
    Args:
        precision: Desired precision
        
    Returns:
        The value of zeta(5)
    """
    # For zeta(5), use parameters (2, -3, 0)
    alpha, beta, r = 2, -3, 0
    max_m = int(-math.log10(precision) * 2) + 15
    
    # The identity H_{2,-3,0}(log(t)^4)(1) = 24*zeta(5) - 10*pi^2*zeta(3) + ...
    h_action = hasse_log_power(4, 1, max_m, alpha, beta, r)
    
    # Get zeta(3)
    zeta3_val = zeta3(precision)
    
    # Extract zeta(5) from the identity
    zeta5 = (h_action + 10 * math.pi**2 * zeta3_val) / 24
    
    return zeta5

def odd_zeta(n: int, precision: float = 1e-15) -> float:
    """
    Compute zeta(2n+1) for positive integer n.
    
    Args:
        n: Parameter such that 2n+1 is the zeta argument
        precision: Desired precision
        
    Returns:
        The value of zeta(2n+1)
    """
    if n == 0:
        raise ValueError("n must be positive")
    
    if n == 1:
        return zeta3(precision)
    if n == 2:
        return zeta5(precision)
    
    # For higher odd zeta values, use the general formula
    s = 2*n + 1
    
    # Parameters depend on whether s = 4k+1 or s = 4k+3
    if s % 4 == 1:
        # For zeta(4k+1)
        alpha = s // 2 - 1
        beta = -s // 2
    else:
        # For zeta(4k+3)
        alpha = s // 2
        beta = -s // 2 - 1
    
    r = 0
    max_m = int(-math.log10(precision) * 3) + 2*n + 10
    
    # Compute the necessary Hasse operator action
    # This is a simplified approach for odd zeta values
    h_action = hasse_log_power(2*n, 1, max_m, alpha, beta, r)
    
    # Adjust based on the specific identity for zeta(2n+1)
    # This is an approximation that works for small n
    factorial_term = math.factorial(2*n)
    coefficient = factorial_term / ((-1)**n * 2)
    
    return h_action / coefficient
