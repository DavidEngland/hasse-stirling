"""
Tests for zeta function computation.
"""

import unittest
import math
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from zeta import zeta3, zeta5, odd_zeta

class TestZetaValues(unittest.TestCase):
    
    def test_zeta3(self):
        # Test ζ(3) against known value (Apéry's constant)
        apery = 1.2020569031595942853997381615114499907649862923405
        result = zeta3()
        self.assertAlmostEqual(result, apery, places=10)
    
    def test_zeta5(self):
        # Test ζ(5) against known value
        zeta5_known = 1.0369277551433699263313654864570341680570809195019
        result = zeta5()
        self.assertAlmostEqual(result, zeta5_known, places=10)
    
    def test_odd_zeta_values(self):
        # Test various odd zeta values against known values
        known_values = {
            1: 1.2020569031595942,  # ζ(3)
            2: 1.0369277551433699,  # ζ(5)
            3: 1.0083492773819228,  # ζ(7)
            4: 1.0020083928260822,  # ζ(9)
        }
        
        for n, expected in known_values.items():
            result = odd_zeta(n)
            self.assertAlmostEqual(result, expected, places=8)
    
    def test_even_odd_pattern(self):
        # Test that our method correctly distinguishes between ζ(4k+1) and ζ(4k+3)
        # Compute using both methods and ensure consistency
        for n in range(1, 5):
            s = 2 * n + 1
            result = odd_zeta(n)
            
            # Check that the value is between 1 and 2
            # (all odd zeta values for positive s > 1 are in this range)
            self.assertTrue(1 < result < 2)
            
            # Specific cases
            if s == 3:
                self.assertAlmostEqual(result, zeta3(), places=10)
            elif s == 5:
                self.assertAlmostEqual(result, zeta5(), places=10)

class TestZetaConvergence(unittest.TestCase):
    
    def test_precision_impact(self):
        # Test that increasing precision improves results
        low_prec = zeta3(precision=1e-8)
        high_prec = zeta3(precision=1e-12)
        
        apery = 1.2020569031595942853997381615114499907649862923405
        
        # Higher precision should be closer to the exact value
        self.assertLessEqual(abs(high_prec - apery), abs(low_prec - apery))
    
    def test_modulo_four_pattern(self):
        # Test that ζ(4k+1) and ζ(4k+3) follow different patterns
        # By checking error convergence rates
        
        # Compute with different precision levels
        precisions = [1e-8, 1e-10, 1e-12]
        
        # For ζ(5) (4k+1 case)
        zeta5_errors = []
        zeta5_known = 1.0369277551433699263313654864570341680570809195019
        
        for prec in precisions:
            result = zeta5(precision=prec)
            error = abs(result - zeta5_known)
            zeta5_errors.append(error)
        
        # For ζ(7) (4k+3 case)
        zeta7_errors = []
        zeta7_known = 1.0083492773819228268397975498497967595998635605680
        
        for prec in precisions:
            result = odd_zeta(3, precision=prec)
            error = abs(result - zeta7_known)
            zeta7_errors.append(error)
        
        # Check that error ratios are consistent with theoretical predictions
        # The 4k+3 case should converge differently than the 4k+1 case
        ratio5 = zeta5_errors[0] / zeta5_errors[-1]
        ratio7 = zeta7_errors[0] / zeta7_errors[-1]
        
        # The ratios should be different due to different parameter patterns
        self.assertNotAlmostEqual(ratio5, ratio7, places=1)

if __name__ == '__main__':
    unittest.main()
