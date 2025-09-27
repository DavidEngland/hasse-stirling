"""
Implementation of Stieltjes constants computation using the Hasse-Stirling framework.
"""

import math
from .hasse_stirling import compute_hasse_coefficients, hasse_log_power

def estimate_max_m_for_stieltjes(k: int, target_precision: float = 1e-15) -> int:
    """
    Estimate the required truncation order for Stieltjes constant computation.
    
    Args:
        k: Index of the Stieltjes constant
        target_precision: Desired precision
        
    Returns:
        Estimated truncation order
    """
    log_precision = -math.log10(target_precision)
    if k <= 5:
        return int(log_precision * 1.5) + 5
    else:
        return int(log_precision * (1 + 0.1*k)) + k + 5

def stieltjes_constant(k: int, precision: float = 1e-15, use_polylog: bool = False) -> float:
    """
    Compute the kth Stieltjes constant using the Hasse operator approach.
    
    Args:
        k: Index of the Stieltjes constant
        precision: Desired precision
        use_polylog: Whether to use the polylogarithm approach (more stable around poles)
        
    Returns:
        The Stieltjes constant gamma_k
    """
    if use_polylog:
        try:
            from .polylog import stieltjes_via_polylog
            return stieltjes_via_polylog(k, precision)
        except ImportError:
            # Fall back to the standard approach if polylog module is not available
            pass
    
    if k == 0:
        # For gamma_0 (Euler's constant), use special parameterization
        alpha, beta, r = 1, -1, 0
    else:
        # For higher Stieltjes constants, use optimized parameters
        alpha = (k + 3) // 2
        beta = -(k + 4) // 2
        r = 0
    
    max_m = estimate_max_m_for_stieltjes(k, precision)
    
    # Apply the parameterized Hasse operator to log(t)^(k+1)
    result = hasse_log_power(k+1, 1, max_m, alpha, beta, r)
    
    return -result / (k + 1)

def compute_stieltjes_constants(k_max: int, precision: float = 1e-15, use_polylog: bool = False) -> list:
    """
    Compute Stieltjes constants from gamma_0 to gamma_k_max.
    
    Args:
        k_max: Maximum index
        precision: Desired precision
        use_polylog: Whether to use the polylogarithm approach (more stable around poles)
        
    Returns:
        List of Stieltjes constants
    """
    return [stieltjes_constant(k, precision, use_polylog) for k in range(k_max + 1)]
