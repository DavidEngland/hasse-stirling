# Hasse-Stirling Framework Examples

This directory contains examples demonstrating practical applications of the Hasse-Stirling framework for computational mathematics.

## Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/generalized-factorials-stirling.git
   cd generalized-factorials-stirling
   ```

2. **Install dependencies**:
   
   Navigate to the zeta examples directory:
   ```bash
   cd hasse-stirling/examples/zeta
   ```
   
   Then install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   
   Or install individual packages directly:
   ```bash
   pip install numpy matplotlib mpmath sympy pandas scipy
   ```

3. **Verify installation**:
   ```bash
   python -c "import numpy, matplotlib, mpmath; print('Installation successful!')"
   ```

## Available Examples

### Riemann Zeta Function Zeros (`riemann_zeros.py`)

This example demonstrates using the Hasse-Stirling framework concepts to explore the non-trivial zeros of the Riemann zeta function. Key features:

- Explores the theoretical connection between zeta zeros and the Hasse-Stirling framework
- Demonstrates how special function representations can provide insights into zero distribution
- Compares with traditional computational methods for finding zeta zeros

The implementation assumes the Riemann Hypothesis (all non-trivial zeros have real part 1/2) for simplicity, but the approach could be extended to explore the critical strip more generally.

**Educational Value:**
- Illustrates connections between different branches of mathematical analysis
- Demonstrates how operator frameworks can be applied to number theory problems
- Provides a starting point for further exploration of zeta function properties

**Practical Considerations:**
- The current implementation is primarily for educational purposes
- Traditional methods are typically more efficient for direct computation of zeta zeros
- The framework shows its strength more in asymptotic analysis than raw computation

## Running the Examples

To run an example:

```bash
# Make sure you're in the zeta directory
cd /path/to/generalized-factorials-stirling/hasse-stirling/examples/zeta

# Run the example
python riemann_zeros.py
```

Each example includes performance benchmarks and visualizations to help understand the advantages of the Hasse-Stirling approach.

## Viewing Results

The examples generate both console output and visualization files:

- Performance comparisons are saved as PNG files in the current directory
- Detailed numerical results are printed to the console
- For high-precision results, the mpmath library is used with 50 digits of precision

## Troubleshooting

If you encounter import errors:
If you encounter import errors:
