# Unified Hasse–Stirling Operator Table

| Function \(f(t)\) | Parameters \((\alpha,\beta,r)\) | \(\mathcal{H}_{\alpha,\beta,r}(f)(x)\) | Known expression / interpretation |
|---|---|---|---|
| \(t^n\) | (0, 1, 0) | \(\mathcal{H}_{0,1,0}(t^n)(x)\) | \(B_n(x)/n!\) (Bernoulli polynomial) |
| \(x^n\) | (0, 1, 0) | \(\mathcal{H}_{0,1,0}(x^n)(0)\) | \(B_n/n!\) (Bernoulli number) |
| \(e^{z t}\) | (0, 1, 0) | \(\mathcal{H}_{0,1,0}(e^{z t})(x)\) | \(\tfrac{z e^{z x}}{e^z - 1}\) (Bernoulli EGF) |
| \(a^{t x}\) | (0, 1, 0) | \(\sum_{m\ge 0} \mathcal{H}_m(a^{t x})\) | \(\tfrac{\log(a^t)\,a^{t x}}{a^t - 1}\) |
| \(e^{t x}\) | (0, 1, 0) | \(\sum_{m\ge 0} \mathcal{H}_m(e^{t x})\) | \(\tfrac{t e^{t x}}{e^t - 1}\) |
| \(e^{z t}\) | (a, −b, 0) | \(\mathcal{H}_{a,−b,0}(e^{z t})(1)\) | \({}_1F_1(a; b; z)\) (confluent hypergeometric) |
| \(\tfrac{1}{(1 − z t)^b}\) | (a, c − a − b, 0) | \(\mathcal{H}_{a,c−a−b,0}((1 − z t)^{−b})(1)\) | \({}_2F_1(a, b; c; z)\) (Gauss hypergeometric) |
| \(e^{−z^2 t/4}\) | (ν + 1, −1, 0) | \(\mathcal{H}_{\nu+1,−1,0}(e^{−z^2 t/4})(1)\) | \(\tfrac{\Gamma(\nu+1)}{(z/2)^\nu} J_\nu(z)\) (Bessel J) |
| \(\log(t)\) | (1, −1, 0) | \(\mathcal{H}_{1,−1,0}(\log t)(x − 1)\) | \(\psi(x) + \gamma\) (digamma) |
| \(\log(t)^{k+1}\) | \(\big(\tfrac{k+3}{2}, −\tfrac{k+4}{2}, 0\big)\) | \(-\tfrac{1}{k+1}\,\mathcal{H}_{\frac{k+3}{2},−\frac{k+4}{2},0}(\log^{k+1} t)(1)\) | \(\gamma_k\) (Stieltjes constant) |
| \(\log(t)^2\) | (1, −2, 0) | \(\mathcal{H}_{1,−2,0}(\log^2 t)(1)\) | \(2\zeta(3) + \gamma^2 + \tfrac{\pi^2}{6}\) |
| \(\log(t)^4\) | (2, −3, 0) | \(\mathcal{H}_{2,−3,0}(\log^4 t)(1)\) | \(24\zeta(5) − 10\pi^2 \zeta(3)\) |
| \(x^{1−s}\) | (α, β, r) | \(\mathcal{H}_{\alpha,\beta,r}(x^{1−s})\) | \((s − 1)\zeta(s, x)\) (Hurwitz zeta; \(s\) complex) |
| \(x^{1−s}\chi(x)\) | (α, β, r) | \(\mathcal{H}_{\alpha,\beta,r}(x^{1−s}\chi(x))\) | \((s − 1)L(s, \chi)\) (Dirichlet L-function, primitive character \(\chi\)) |
| \(\log \Gamma(x)\) | (1, −1, 0) | integrate \(\mathcal{H}_{1,−1,0}(\log t)(x − 1)\) | \(\log \Gamma(x)\) |
| \(\log G(x)\) | (1, −1, 0) | integrate \(\mathcal{H}_{1,−1,0}(\log^2 t)(x − 1)\) | \(\log G(x)\) (Barnes G) |
| \(\log^m(t)\) (derivatives) | (1, −1, 0) | successive derivatives wrt \(x\) | \(\psi^{(m)}(x)\) (polygamma functions) |

---

### Notes

- **Dirichlet L-functions:**
  By twisting the Hurwitz zeta entry with a Dirichlet character \(\chi\), the operator yields \((s-1)L(s,\chi)\). This is the natural generalization of the Hurwitz zeta case.

- **Polygammas:**
  Since \(\psi^{(m)}(x) = \tfrac{d^m}{dx^m}\psi(x)\), and \(\psi(x)\) itself comes from the \(\log t\) entry, higher derivatives of the operator output give the polygammas. Equivalently, higher powers of \(\log t\) under tuned parameters yield the same constants.

- **r parameter:**
  All entries are written for \(r=0\). Nonzero \(r\) shifts the weighting in the double sum but does not change the essential identities when parameters are adjusted.

- **Coefficient recurrence:**
  The Hasse–Stirling coefficients \(H_{m,n}\) satisfy
  \[
  H_{m+1,n} = H_{m,n-1} - \frac{m+1-n}{m+2}\,H_{m,n}, \quad 1 \le n \le m+1,
  \]
  with boundary \(H_{m,0} = \tfrac{1}{m+1}\).

---

