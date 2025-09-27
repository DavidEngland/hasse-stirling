"""
Example of computing Stieltjes constants using the Hasse-Stirling approach.
"""

import sys
import os
import matplotlib.pyplot as plt
import numpy as np
import time

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from stieltjes import compute_stieltjes_constants

def main():
    # Compute Stieltjes constants
    print("Computing Stieltjes constants...")
    k_max = 15
    
    start_time = time.time()
    gamma_values = compute_stieltjes_constants(k_max)
    end_time = time.time()
    
    print(f"Computation completed in {end_time - start_time:.4f} seconds.")
    
    # Print the values
    print("\nStieltjes constants:")
    for k, gamma_k in enumerate(gamma_values):
        print(f"γ_{k} = {gamma_k:.15f}")
    
    # Plot the values
    plt.figure(figsize=(12, 6))
    k_values = np.arange(k_max + 1)
    plt.scatter(k_values, gamma_values, s=50)
    
    # Connect with lines
    plt.plot(k_values, gamma_values, 'k--', alpha=0.5)
    
    plt.xlabel('k')
    plt.ylabel('γ_k')
    plt.title('Stieltjes Constants')
    plt.grid(True, alpha=0.3)
    
    # Add horizontal line at y=0
    plt.axhline(y=0, color='r', linestyle='-', alpha=0.3)
    
    # Annotate some points
    for k in [0, 1, 2, 5, 10]:
        if k <= k_max:
            plt.annotate(f'γ_{k}', 
                         xy=(k, gamma_values[k]), 
                         xytext=(5, 10),
                         textcoords='offset points')
    
    plt.tight_layout()
    
    # Save or show the plot
    plt.savefig('stieltjes_constants.png')
    print("\nPlot saved as 'stieltjes_constants.png'")
    plt.show()

if __name__ == "__main__":
    main()
