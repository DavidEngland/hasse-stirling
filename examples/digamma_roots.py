"""
Example of computing roots of the digamma function using the Hasse-Stirling approach.
"""

import sys
import os
import matplotlib.pyplot as plt
import numpy as np
import time

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from special_roots import find_digamma_roots, digamma_asymptotic_root

def main():
    # Compute the first 20 roots
    print("Computing the first 20 roots of the digamma function...")
    start_time = time.time()
    roots = find_digamma_roots(20)
    end_time = time.time()
    
    print(f"Computation completed in {end_time - start_time:.4f} seconds.")
    
    # Print the first few roots
    print("\nFirst 10 digamma roots:")
    for i, root in enumerate(roots[:10]):
        print(f"ψ(x_{i+1}) = 0 at x_{i+1} = {root:.15f}")
    
    # Compare with asymptotic formula
    print("\nComparison with asymptotic formula:")
    for i in range(5):
        n = i + 1
        asymp = digamma_asymptotic_root(n, terms=4)
        print(f"Root #{n}: Exact = {roots[i]:.10f}, Asymptotic = {asymp:.10f}, Diff = {abs(roots[i] - asymp):.2e}")
    
    # Plot the roots
    plt.figure(figsize=(12, 6))
    
    # Plot exact roots
    n_values = np.arange(1, len(roots) + 1)
    plt.scatter(n_values, roots, s=50, label='Exact roots')
    
    # Plot asymptotic approximation
    n_range = np.linspace(1, len(roots), 100)
    asymp_approx = [digamma_asymptotic_root(n, terms=1) for n in n_range]
    plt.plot(n_range, asymp_approx, 'r--', label='First-order approximation')
    
    # Higher-order approximation
    asymp_approx4 = [digamma_asymptotic_root(n, terms=4) for n in n_range]
    plt.plot(n_range, asymp_approx4, 'g-.', label='Fourth-order approximation')
    
    plt.xlabel('Root index n')
    plt.ylabel('Root value')
    plt.title('Roots of the Digamma Function')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    
    # Save or show the plot
    plt.savefig('digamma_roots.png')
    print("\nPlot saved as 'digamma_roots.png'")
    plt.show()

if __name__ == "__main__":
    main()
