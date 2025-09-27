# Expansion of the Hurwitz Zeta Function at $x = \frac{1}{2}$

The Hurwitz zeta function is defined as:
\[
\zeta(s, x) = \sum_{n=0}^{\infty} \frac{1}{(n + x)^s}
\]
for $\operatorname{Re}(s) > 1$ and $x > 0$.

## Laurent Expansion at $x = \frac{1}{2}$

The Laurent expansion about $s=1$ at $x = \frac{1}{2}$ is:
\[
\zeta(s, \tfrac{1}{2}) = \frac{1}{s-1} + \sum_{k=0}^{\infty} \frac{(-1)^k}{k!} \gamma_k\left(\tfrac{1}{2}\right) (s-1)^k
\]
where $\gamma_k\left(\tfrac{1}{2}\right)$ are the Stieltjes constants evaluated at $x = \frac{1}{2}$.

## Hasse-Stirling Representation for $\gamma_k\left(\frac{1}{2}\right)$

The Stieltjes constants at $x = \frac{1}{2}$ can be computed using the Hasse-Stirling operator:
\[
\gamma_k\left(\tfrac{1}{2}\right) = -\frac{1}{k+1} \mathcal{H}_{\frac{k+3}{2}, -\frac{k+4}{2}, 0}\left([\log(t)]^{k+1}\right)\left(\tfrac{1}{2}\right)
\]
where the operator acts on $f(t) = [\log(t)]^{k+1}$ evaluated at $t = \frac{1}{2}$.

## Explicit Series Expansion

\[
\zeta(s, \tfrac{1}{2}) = \frac{1}{s-1} + \sum_{k=0}^{\infty} \frac{(-1)^k}{k!} \left[ -\frac{1}{k+1} \sum_{m=0}^{\infty} \sum_{n=0}^{m} H_{m,n}^{\frac{k+3}{2}, -\frac{k+4}{2}, 0} \left(\log(n + \tfrac{3}{2})\right)^{k+1} \right] (s-1)^k
\]

## Notes

- The only change from the $x=1$ case is to replace all instances of $1$ with $1/2$ in the evaluation argument.
- The Hasse-Stirling coefficients $H_{m,n}^{\alpha,\beta,r}$ are unchanged; only the evaluation point for the function argument changes.
- This expansion converges rapidly for $|s-1|$ small and can be used to compute $\zeta(s, \tfrac{1}{2})$ and its derivatives near $s=1$.

## Example: First Stieltjes Constant at $x = \frac{1}{2}$

\[
\gamma_0\left(\tfrac{1}{2}\right) = -\mathcal{H}_{\frac{3}{2}, -2, 0}(\log(t))\left(\tfrac{1}{2}\right)
\]

## Further Directions

- The same approach applies for any $x > 0$; simply evaluate the Hasse-Stirling operator at the desired $x$.
- For $x = \frac{1}{2}$, the expansion is especially useful for applications in modular forms and theta functions, where half-integer arguments naturally arise.