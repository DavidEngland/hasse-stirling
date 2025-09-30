# Hasse–Stirling Operator Cheatsheet

\[
\mathcal{H}_{\alpha,\beta,r}(f)(x) \;=\; \sum_{m=0}^\infty \sum_{n=0}^m H_{m,n}^{\alpha,\beta,r}\,(x+n)^{1-\alpha-\beta+r+n}\, f^{(n)}(x+n)
\]

**Coefficient recurrence:**
\[
H_{m+1,n} = H_{m,n-1} - \frac{m+1-n}{m+2}\,H_{m,n}, \quad H_{m,0}=\tfrac{1}{m+1}.
\]

---

| \(f(t)\) | \((\alpha,\beta,r)\) | \(\mathcal{H}_{\alpha,\beta,r}(f)(x)\) | Expression |
|---|---|---|---|
| \(t^n\) | (0,1,0) | \(\tfrac{B_{n+1}(x)}{n+1}\) | Bernoulli polynomials (Faulhaber) |
| \(t^n\) | (1,1,0) | \(\tfrac{E_n(x)}{2}\) | Euler polynomials (alternating sums) |
| \(1\) | (0,1,0) | \(x\) | Identity |
| \(e^{z t}\) | (0,1,0) | \(\tfrac{z e^{z x}}{e^z-1}\) | Bernoulli EGF |
| \(e^{z t}\) | (1,1,0) | \(\tfrac{e^{z x}}{1+e^z}\) | Euler EGF |
| \((1-zt)^{-b}\) | (a,c−a−b,0) | \({}_2F_1(a,b;c;z)\) | Gauss hypergeometric |
| \(e^{z t}\) | (a,−b,0) | \({}_1F_1(a;b;z)\) | Confluent hypergeometric |
| \(e^{-z^2 t/4}\) | (ν+1,−1,0) | \(\tfrac{\Gamma(\nu+1)}{(z/2)^\nu} J_\nu(z)\) | Bessel \(J_\nu\) |
| \(\log t\) | (1,0,0) | \(\log \Gamma(x)\) | Log-gamma |
| \(\log t\) | (1,−1,0) | \(\psi(x)+\gamma\) | Digamma |
| \(\log^{k+1} t\) | \(\big(\tfrac{k+3}{2},-\tfrac{k+4}{2},0\big)\) | \(\gamma_k\) | Stieltjes constants |
| \(\log^2 t\) | (1,−2,0) | \(2\zeta(3)+\gamma^2+\tfrac{\pi^2}{6}\) | Odd zeta combo |
| \(\log^4 t\) | (2,−3,0) | \(24\zeta(5)-10\pi^2\zeta(3)\) | Odd zeta combo |
| \(\log\!\tfrac{1+t}{1-t}\) | (1,1,0) | Catalan’s \(\beta(0)\) | Dirichlet beta / Euler numbers |
| \(x^{1-s}\) | (α,β,r) | \((s-1)\zeta(s,x)\) | Hurwitz zeta |
| \(x^{1-s}\chi(x)\) | (α,β,r) | \((s-1)L(s,\chi)\) | Dirichlet \(L\)-function |
| \(\tfrac{t^{s-1}}{e^t/z-1}\) | (1,0,0) | \(\Gamma(s)\,\mathrm{Li}_s(z)\) | Polylogarithm |
| \(t^{s-1}\) | (1,0,0) | \(\tfrac{\Gamma(s)}{s-1}\Gamma(1-s,x)\) | Incomplete gamma |
| \(t^{-s}\) | (1,0,0) | \(\zeta(s,x)-\tfrac{x^{1-s}}{s-1}\) | Hurwitz zeta remainder |
| \(\log G(x)\) | (1,−1,0) | \(\log G(x)\) | Barnes \(G\) |
| derivatives of \(\log t\) | (1,−1,0) | \(\psi^{(m)}(x)\) | Polygammas |

---

### 🗝️ Notes
- **Regimes:** (0,1,0) Bernoulli sums; (1,1,0) Euler/alternating sums; (1,0,0) Gamma/incomplete gamma.
- **\(r\)-parameter:** shifts combinatorial backbone (via \(r\)-Stirling numbers), giving weighted Faulhaber/Euler analogues.
- **Triangle:** zeta \(\leftrightarrow\) Dirichlet \(L\) \(\leftrightarrow\) polylogarithm all realized via \(\mathcal{H}\).