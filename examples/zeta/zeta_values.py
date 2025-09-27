"""
Example of computing zeta values using the Hasse-Stirling approach.
"""

import sys
import os
import matplotlib.pyplot as plt
import numpy as np
import time

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from zeta import zeta3, zeta5, odd_zeta

def main():
    # Compute specific zeta values
    print("Computing zeta values...")
    
    start_time = time.time()
    zeta3_val = zeta3()
    zeta5_val = zeta5()
    end_time = time.time()
    
    print(f"ζ(3) = {zeta3_val:.15f}")
    print(f"ζ(5) = {zeta5_val:.15f}")
    print(f"Computation completed in {end_time - start_time:.4f} seconds.")
    
    # Compute a range of odd zeta values
    print("\nComputing odd zeta values...")
    n_max = 8  # Up to ζ(17)
    odd_zetas = []
    
    start_time = time.time()
    for n in range(1, n_max + 1):
        zeta_val = odd_zeta(n)
        odd_zetas.append(zeta_val)
        print(f"ζ({2*n+1}) = {zeta_val:.15f}")
    end_time = time.time()
    
    print(f"Computation completed in {end_time - start_time:.4f} seconds.")
    
    # Plot the values
    plt.figure(figsize=(12, 6))
    n_values = 2 * np.arange(1, n_max + 1) + 1
    plt.scatter(n_values, odd_zetas, s=50)
    
    # Connect with lines
    plt.plot(n_values, odd_zetas, 'k--', alpha=0.5)
    
    plt.xlabel('s')
    plt.ylabel('ζ(s)')
    plt.title('Odd Zeta Values ζ(2n+1)')
    plt.grid(True, alpha=0.3)
    
    # Add horizontal line at y=1
    plt.axhline(y=1, color='r', linestyle='-', alpha=0.3)
    
    # Annotate some points
    for i, n in enumerate([3, 5, 7]):
        idx = (n - 3) // 2
        if idx < len(odd_zetas):
            plt.annotate(f'ζ({n})', 
                         xy=(n, odd_zetas[idx]), 
                         xytext=(5, 10),
                         textcoords='offset points')
    
    plt.tight_layout()
    
    # Save or show the plot
    plt.savefig('odd_zeta_values.png')
    print("\nPlot saved as 'odd_zeta_values.png'")
    plt.show()

if __name__ == "__main__":
    main()
