"""
Tests for core functionality of the Hasse-Stirling framework.
"""

import unittest
import math
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from hasse_stirling import (
    binomial, generalized_stirling, compute_hasse_coefficients,
    hasse_operator_action, hasse_log_power
)

class TestBinomial(unittest.TestCase):
    
    def test_basic_values(self):
        self.assertEqual(binomial(5, 2), 10)
        self.assertEqual(binomial(10, 0), 1)
        self.assertEqual(binomial(10, 10), 1)
    
    def test_symmetry(self):
        for n in range(1, 10):
            for k in range(n + 1):
                self.assertEqual(binomial(n, k), binomial(n, n - k))
    
    def test_edge_cases(self):
        self.assertEqual(binomial(5, 6), 0)  # k > n
        self.assertEqual(binomial(5, -1), 0)  # k < 0

class TestGeneralizedStirling(unittest.TestCase):
    
    def test_standard_stirling_second_kind(self):
        # Test against known values of Stirling numbers of the second kind
        known_values = {
            (0, 0): 1,
            (1, 1): 1,
            (2, 1): 1,
            (2, 2): 1,
            (3, 1): 1,
            (3, 2): 3,
            (3, 3): 1,
            (4, 1): 1,
            (4, 2): 7,
            (4, 3): 6,
            (4, 4): 1,
        }
        
        for (n, k), expected in known_values.items():
            self.assertEqual(generalized_stirling(n, k, 0, 1, 0), expected)
    
    def test_standard_stirling_first_kind(self):
        # Test against known values of unsigned Stirling numbers of the first kind
        known_values = {
            (0, 0): 1,
            (1, 1): 1,
            (2, 1): 1,
            (2, 2): 1,
            (3, 1): 2,
            (3, 2): 3,
            (3, 3): 1,
            (4, 1): 6,
            (4, 2): 11,
            (4, 3): 6,
            (4, 4): 1,
        }
        
        for (n, k), expected in known_values.items():
            self.assertEqual(generalized_stirling(n, k, 1, 0, 0), expected)
    
    def test_r_stirling_second_kind(self):
        # Test r-Stirling numbers (r=2)
        # S_2(n,k) - 2-Stirling numbers of the second kind
        known_values = {
            (2, 2): 1,
            (3, 2): 2,
            (3, 3): 1,
            (4, 2): 4,
            (4, 3): 5,
            (4, 4): 1,
        }
        
        for (n, k), expected in known_values.items():
            # r-Stirling numbers require special handling through initial conditions
            # This is an approximation using the recurrence with r as the parameter
            self.assertEqual(generalized_stirling(n, k, 0, 1, 2), expected)
    
    def test_recurrence_relation(self):
        # Test the recurrence relation for generalized Stirling numbers
        alpha, beta, r = 2, -3, 1
        n, k = 5, 3
        
        # S(n,k;α,β,r) = S(n-1,k-1;α,β,r) + (βk - αn + r)S(n-1,k;α,β,r)
        expected = (
            generalized_stirling(n-1, k-1, alpha, beta, r) + 
            (beta*k - alpha*n + r) * generalized_stirling(n-1, k, alpha, beta, r)
        )
        
        self.assertEqual(generalized_stirling(n, k, alpha, beta, r), expected)
    
    def test_edge_cases(self):
        self.assertEqual(generalized_stirling(5, 6, 1, 1, 0), 0)  # k > n
        self.assertEqual(generalized_stirling(5, -1, 1, 1, 0), 0)  # k < 0

class TestHasseCoefficients(unittest.TestCase):
    
    def test_standard_hasse_coefficients(self):
        # Test standard Hasse coefficients (α=0, β=1, r=0)
        H = compute_hasse_coefficients(3)
        
        # Known values for standard Hasse coefficients
        expected = [
            [1],           # H[0][0]
            [1/2, -1/2],   # H[1][0], H[1][1]
            [1/3, -1/3, 1/6], # H[2][0], H[2][1], H[2][2]
            [1/4, -3/8, 1/4, -1/24]  # H[3][0], H[3][1], H[3][2], H[3][3]
        ]
        
        for m in range(4):
            for n in range(m + 1):
                self.assertAlmostEqual(H[m][n], expected[m][n], places=12)
    
    def test_recurrence_relation(self):
        # Test the recurrence relation for Hasse coefficients
        alpha, beta, r = 1, -1, 0
        max_m = 5
        
        H = compute_hasse_coefficients(max_m, alpha, beta, r)
        
        for m in range(1, max_m):
            for n in range(1, m + 1):
                expected = H[m-1][n-1] - ((m*alpha + n*beta + r)/(m+2)) * H[m-1][n]
                self.assertAlmostEqual(H[m][n], expected, places=12)

class TestHasseOperator(unittest.TestCase):
    
    def test_bernoulli_identity(self):
        # Test that H(x^n) = B_n(x)/n! for standard Hasse operator
        for n in range(5):
            def f(x):
                return x**n
            
            # For x=1, B_n(1) has simple values
            if n == 0:
                expected = 1
            elif n == 1:
                expected = 1/2
            elif n % 2 == 1:
                expected = 0
            elif n == 2:
                expected = 1/6
            elif n == 4:
                expected = -1/30
            
            result = hasse_operator_action(f, 1, 10)
            self.assertAlmostEqual(result, expected, places=12)
    
    def test_logarithm_action(self):
        # Test action on log(t) - should relate to Euler's constant
        gamma = 0.57721566490153286060651209008240243104215933593992
        
        # H(log(t))(1) = -γ
        result = hasse_log_power(1, 1, 20)
        self.assertAlmostEqual(result, -gamma, places=10)
        
        # Test action on log(t)^2
        # Known value for H(log(t)^2)(1)
        expected = 2 * (gamma**2 + math.pi**2/6)
        result = hasse_log_power(2, 1, 20, 1, -1, 0)
        self.assertAlmostEqual(result / expected, 1.0, places=8)

if __name__ == '__main__':
    unittest.main()
