"""
Tests for Stieltjes constant computation.
"""

import unittest
import math
import sys
import os

# Remove relative import in stieltjes.py for direct script execution
# Instead, use absolute import in stieltjes.py:
# from hasse_stirling import compute_hasse_coefficients, hasse_log_power

# In this test file, ensure stieltjes.py is imported as a module, not as a package
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from stieltjes import stieltjes_constant, compute_stieltjes_constants

class TestStieltjesConstants(unittest.TestCase):
    
    def test_gamma0(self):
        # Test Euler's constant (gamma_0)
        gamma = 0.57721566490153286060651209008240243104215933593992
        result = stieltjes_constant(0)
        self.assertAlmostEqual(result, gamma, places=10)
    
    def test_first_few_constants(self):
        # Test against known values of the first few Stieltjes constants
        known_values = {
            0: 0.57721566490153286,  # Euler's constant
            1: -0.0728158454836767,
            2: -0.0096903631928723,
            3: 0.0020538344203033,
            4: 0.0023253700654673,
        }
        
        for k, expected in known_values.items():
            result = stieltjes_constant(k)
            self.assertAlmostEqual(result, expected, places=8)
    
    def test_batch_computation(self):
        # Test batch computation of Stieltjes constants
        k_max = 5
        constants = compute_stieltjes_constants(k_max)
        
        self.assertEqual(len(constants), k_max + 1)
        
        # Compare with individual computations
        for k in range(k_max + 1):
            individual = stieltjes_constant(k)
            self.assertAlmostEqual(constants[k], individual, places=10)
    
    def test_convergence(self):
        # Test that increasing precision gives better results
        gamma = 0.57721566490153286060651209008240243104215933593992
        
        # Compute with different precision settings
        result1 = stieltjes_constant(0, precision=1e-8)
        result2 = stieltjes_constant(0, precision=1e-12)
        
        # Higher precision should be closer to the exact value
        self.assertLessEqual(abs(result2 - gamma), abs(result1 - gamma))
    
    def test_sign_pattern(self):
        # Test the known sign pattern of the first several constants
        expected_signs = [1, -1, -1, 1, 1, -1]  # Known pattern for first 6
        constants = compute_stieltjes_constants(5)
        
        for k, constant in enumerate(constants):
            expected_sign = expected_signs[k]
            actual_sign = 1 if constant > 0 else -1
            self.assertEqual(actual_sign, expected_sign, f"Wrong sign for gamma_{k}")

class TestStieltjesNumericalStability(unittest.TestCase):
    
    def test_parameter_optimization(self):
        # Test that optimized parameters produce better results than standard ones
        k = 10  # For higher k, parameter optimization is crucial
        
        # Standard Hasse approach
        def compute_standard(k):
            alpha, beta, r = 0, 1, 0
            max_m = 30
            from hasse_stirling import hasse_log_power
            result = hasse_log_power(k+1, 1, max_m, alpha, beta, r)
            return -result / (k + 1)
        
        # Optimized approach (from stieltjes.py)
        optimized_result = stieltjes_constant(k)
        standard_result = compute_standard(k)
        
        # We expect the optimized version to be more stable
        # Compare with a known value or approximation for gamma_10
        approx_gamma10 = -0.000008673655  # Approximate value from literature
        
        opt_error = abs(optimized_result - approx_gamma10)
        std_error = abs(standard_result - approx_gamma10)
        
        # The optimized version should have lower error
        self.assertLess(opt_error, std_error)
    
    def test_polylogarithm_reformulation(self):
        # This test checks a potential polylogarithm-based implementation
        # for better handling of log poles
        
        # Note: This requires implementing a polylogarithm-based approach
        # Pending implementation
        pass

if __name__ == '__main__':
    unittest.main()
