| Function \(f(t)\) | Parameters \((\alpha,\beta,r)\) | \(\mathcal{H}_{\alpha,\beta,r}(f)(x)\) | Known expression / interpretation |
|---|---|---|---|
| \(t^n\) | (0,1,0) | \(\tfrac{B_{n+1}(x)}{n+1}\) | Integrated Bernoulli polynomial (Faulhaber) |
| \(x^n\) | (0,1,0) | \(\tfrac{B_n}{n!}\) | Bernoulli number |
| \(1\) | (0,1,0) | \(x\) | Identity |
| \(e^{z t}\) | (0,1,0) | \(\tfrac{z e^{z x}}{e^z-1}\) | Bernoulli EGF |
| \(a^{t x}\) | (0,1,0) | \(\tfrac{\log(a^t)\,a^{t x}}{a^t-1}\) | Generalized Bernoulli EGF |
| \(e^{t x}\) | (0,1,0) | \(\tfrac{t e^{t x}}{e^t-1}\) | Classical Bernoulli EGF |
| \(e^{z t}\) | (1,1,0) | \(\tfrac{e^{z x}}{1+e^z}\) | Euler polynomial EGF (alternating sums) |
| \(t^n\) | (1,1,0) | \(\tfrac{E_n(x)}{2}\) | Euler polynomial |
| \(e^{z t}\) | (a,−b,0) | \({}_1F_1(a;b;z)\) | Confluent hypergeometric |
| \((1-zt)^{-b}\) | (a,c−a−b,0) | \({}_2F_1(a,b;c;z)\) | Gauss hypergeometric |
| \(e^{-z^2 t/4}\) | (ν+1,−1,0) | \(\tfrac{\Gamma(\nu+1)}{(z/2)^\nu} J_\nu(z)\) | Bessel \(J_\nu\) |
| \(\log t\) | (1,−1,0) | \(\psi(x)+\gamma\) | Digamma |
| \(\log^{k+1} t\) | \(\big(\tfrac{k+3}{2},-\tfrac{k+4}{2},0\big)\) | \(\gamma_k\) | Stieltjes constants |
| \(\log^2 t\) | (1,−2,0) | \(2\zeta(3)+\gamma^2+\tfrac{\pi^2}{6}\) | Odd zeta combo |
| \(\log^4 t\) | (2,−3,0) | \(24\zeta(5)-10\pi^2\zeta(3)\) | Odd zeta combo |
| \(x^{1-s}\) | (α,β,r) | \((s-1)\zeta(s,x)\) | Hurwitz zeta (complex \(s\)) |
| \(x^{1-s}\chi(x)\) | (α,β,r) | \((s-1)L(s,\chi)\) | Dirichlet \(L\)-function (primitive \(\chi\)) |
| \(t^{s-1}\) | (1,0,0) | \(\tfrac{\Gamma(s)}{s-1}\Gamma(1-s,x)\) | Incomplete gamma |
| \(t^{-s}\) | (1,0,0) | \(\zeta(s,x)-\tfrac{x^{1-s}}{s-1}\) | Hurwitz zeta remainder |
| \(\log \Gamma(x)\) | (1,0,0) | \(\log \Gamma(x)\) | via integrating digamma |
| \(\log G(x)\) | (1,−1,0) | \(\log G(x)\) | Barnes \(G\) (up to normalization) |
| \(\log t\) (derivatives) | (1,−1,0) | \(\psi^{(m)}(x)\) | Polygamma functions |
| \(\dfrac{t^{s-1}}{e^t/z-1}\) | (1,0,0) | \(\Gamma(s)\,\mathrm{Li}_s(z)\) | Polylogarithm; completes zeta–\(L\)–polylog triangle |
| Notes: \(r\) parameter | — | — | Most entries use \(r=0\). Nonzero \(r\) shifts the combinatorial backbone (via \(r\)-Stirling/Bernoulli analogues) and can reweight convergence without changing core identities after parameter alignment. |
| Notes: coefficients | — | — | \(H_{m+1,n}=H_{m,n-1}-\dfrac{m+1-n}{m+2}H_{m,n}\) for \(1\le n\le m+1\), with \(H_{m,0}=\dfrac{1}{m+1}\). |