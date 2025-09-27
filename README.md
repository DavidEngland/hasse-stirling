# Hasse-Stirling Framework

A Python implementation of the Hasse-Stirling computational framework for efficient calculation of special functions.

## Features

- Generalized Hasse operator with flexible parameterization $(\alpha, \beta, r)$
- Generalized Stirling numbers computation (Hsu-Shiue recurrence)
- Symmetric/self-adjoint operator construction for special parameter regimes
- Applications to:
  - Stieltjes constants
  - Zeta values (odd, Hurwitz, and multiple)
  - Digamma and polygamma functions
  - Hypergeometric functions
  - Bessel functions
  - Lambert W function
  - Bernoulli numbers and polynomials
- Support for complex and hypercomplex (quaternionic/Clifford) parameter extensions (see `/complex-extension` and `/physics-applications`)
- Operator tables and cheat sheets for rapid reference
- Homework and educational modules for symmetry, self-adjointness, and physical interpretation

## Usage

Basic usage:

```python
from hasse_stirling import hasse_operator, generalized_stirling

# Compute generalized Stirling numbers
s = generalized_stirling(10, 4, alpha=1, beta=0)  # Stirling number of first kind

# Apply the Hasse operator
result = hasse_operator(lambda x: x**3, 1.0, alpha=0, beta=1)  # Returns B₃(1)/3!
```

See the `examples` directory for advanced applications, including Hurwitz zeta, critical strip analysis, and symmetry/self-adjointness demonstrations.

## Installation

## When to Use Hasse-Stirling

- **Optimal for:** High-precision special functions, large parameter regimes, and functions where series acceleration is critical (e.g., Stieltjes constants, odd zeta values, hypergeometric/Bessel functions).
- **Symmetry/Self-adjointness:** For $\alpha + \beta = 0$ ("hyperbolic strip"), the operator is symmetric/self-adjoint and connects to Hermite polynomial theory.
- **Complex/Hypercomplex Extensions:** Supports complex $s$ for Hurwitz zeta and can be extended to quaternionic/Clifford domains for physics and multidimensional analysis.
- **Physical Interpretation:** Parameters map to affinity, barrier, and bias, with direct analogs in statistical mechanics, quantum theory, and field theory.
- **Limitations:** For critical strip ($0 < \operatorname{Re}(s) < 1$), use functional equation or Riemann-Siegel methods; Hasse-Stirling is best for $\operatorname{Re}(s) > 1$ and analytic continuation.

## What We've Learned

- The Hasse-Stirling operator unifies discrete calculus, special functions, and combinatorics.
- Symmetric weights and self-adjointness are achieved for $\alpha = -\beta$; all three operator tables (original, mirror, symmetric) coincide in this regime.
- The operator provides the correction terms for Euler-Maclaurin summation, enabling rapid analytic continuation for zeta and related functions.
- For Hurwitz zeta with complex $s$, the operator can compute $(s-1)\zeta(s,x)$ via $\mathcal{H}_{\alpha,\beta,r}(x^{1-s})$.
- Extensions to hypercomplex domains (quaternions, Clifford algebras) are possible and open new applications in physics and geometry.
- The framework connects to Hermite polynomials, spectral theory, and quantum mechanics via symmetry and operator structure.

## References

See the main project documentation, `/docs/arXiv-1411.6271v1/GSN.bbl`, and the `/cheatsheet.md` and `/cheatsheet_condensed.md` for formulas, tables, and operational details.

---

