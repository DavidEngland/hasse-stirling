# Surface Roughness, Log Wind Profile, and Geometric Mean Heights

## 1. Neutral Log Profile
Under neutral stratification (ignore stability corrections):
\[
U(z) = \frac{u_*}{\kappa}\,\ln\!\left(\frac{z}{z_0}\right),
\]
where:
- \(u_*\): friction velocity
- \(\kappa \approx 0.40\): von Kármán constant
- \(z_0\): aerodynamic roughness length
- \(z\): measurement height (above displacement height if applicable)

## 2. Averaging Velocities Across Multiple Heights
Let heights \(z_1,\dots,z_N\) and corresponding mean horizontal speeds \(U_i = U(z_i)\). Then:
\[
\bar{U} = \frac{1}{N}\sum_{i=1}^N U(z_i) = \frac{u_*}{\kappa}\left[\frac{1}{N}\sum_{i=1}^N \ln\!\left(\frac{z_i}{z_0}\right)\right]
= \frac{u_*}{\kappa}\ln\!\left(\frac{( \prod_{i=1}^N z_i )^{1/N}}{z_0}\right).
\]
Define the geometric mean height:
\[
z_g = \Big(\prod_{i=1}^N z_i\Big)^{1/N}.
\]
Then:
\[
\bar{U} = U(z_g).
\]
Conclusion: The arithmetic mean of the velocities equals the log-profile velocity evaluated at the geometric mean of heights, not at the arithmetic mean height. Any interpretation of “representative” height for the averaged velocity should use \(z_g\).

## 3. Implication for Roughness and Friction Velocity Estimation
If one regress \(U_i\) against \(\ln z_i\):
\[
U_i = A \ln z_i + B,\quad A = \frac{u_*}{\kappa},\quad B = -\frac{u_*}{\kappa}\ln z_0.
\]
Thus:
- \(u_* = \kappa A\).
- \(z_0 = \exp\!\left(-B/A\right)\).

Averaging velocities first and pairing with an arithmetic mean height biases the inferred \(z_0\) (systematically misrepresents the intercept), especially when heights span orders of magnitude.

## 4. Recommended Procedure
1. Use individual height measurements (do not pre-average across heights).
2. Restrict to neutral periods (e.g., small |Obukhov length|; apply stability corrections otherwise: add \(\psi_m(z/L)\) term).
3. Perform linear regression of \(U\) vs \(\ln z\).
4. Extract \(u_*\) and \(z_0\) from slope and intercept.
5. If reporting a single “representative height” for an averaged velocity, specify \(z_g\), not \(\bar{z}\).

## 5. Practical Notes
- Displacement height \(d\): For tall vegetation, replace \(z\) with \(z-d\) everywhere; geometric mean uses \(z_i-d\).
- Quality control: Exclude low-level sensor data if within roughness sublayer (~first 2–3 \(z_0\)).
- Uncertainty: Propagate regression standard errors to \(u_*\) and \(z_0\); log-space linearity simplifies error estimates.

## 6. Summary
Neutral-layer logarithmic dependence means velocity averaging across levels maps to geometric mean height; roughness and friction velocity estimates should honor the log-linear structure, avoiding arithmetic-height substitutions.

## 7. Implications for Drag Coefficient (C_D)
Definition:
\[
C_D(z) \equiv \frac{\tau}{\tfrac{1}{2}\rho\,U(z)^2} = \left(\frac{u_*}{U(z)}\right)^2.
\]
Under neutral conditions (outside the roughness sublayer) with displacement height \(d\):
\[
U(z) = \frac{u_*}{\kappa}\ln\!\frac{z-d}{z_0}
\quad\Rightarrow\quad
C_D(z) = \left[\frac{\kappa}{\ln\!\frac{z-d}{z_0}}\right]^2.
\]
With stability correction \(\psi_m\):
\[
C_D(z,L) = \left[\frac{\kappa}{\ln\!\frac{z-d}{z_0}-\psi_m(z/L)}\right]^2,
\]
and \(\psi_m\equiv 0\) for neutral.

- Averaging across heights: since \(\bar{U}=U(z_g)\), the drag coefficient implied by the averaged speed is
  \[
  C_D(\bar{U}) = \left[\frac{\kappa}{\ln\!\frac{z_g-d}{z_0}}\right]^2
  \quad(\text{neutral}).
  \]
- Using the arithmetic mean height \( \bar{z} \) instead yields
  \[
  C_D(\bar{z})=\left[\frac{\kappa}{\ln\!\frac{\bar{z}-d}{z_0}}\right]^2
  \le C_D(z_g),
  \]
  because \( \bar{z}\ge z_g \Rightarrow \ln\!\frac{\bar{z}-d}{z_0}\ge \ln\!\frac{z_g-d}{z_0}\).
  Hence pairing \(\bar{U}\) with \(\bar{z}\) systematically underestimates \(C_D\).

Bias (neutral):
\[
\frac{C_D(\bar{z})}{C_D(z_g)}=\left[\frac{\ln\!\frac{z_g-d}{z_0}}{\ln\!\frac{\bar{z}-d}{z_0}}\right]^2 \le 1.
\]
For small spread with \(\delta=\ln\!\frac{\bar{z}}{z_g}\ll 1\) and \(L_g=\ln\!\frac{z_g-d}{z_0}\):
\[
\frac{C_D(\bar{z})}{C_D(z_g)} \approx \left(1-\frac{\delta}{L_g}\right)^2 \approx 1-\frac{2\,\delta}{L_g},
\]
so relative underestimation is approximately \( \approx 2\,\ln(\bar{z}/z_g)/\ln((z_g-d)/z_0)\).

Recommended workflow:
1. Estimate \(u_*\) and \(z_0\) by regressing \(U\) on \(\ln(z-d)\) (or include \(\psi_m\) when non-neutral).
2. Choose a reference height \(z_{\mathrm{ref}}\) and compute
   \[
   C_D(z_{\mathrm{ref}})=\left[\frac{\kappa}{\ln\!\frac{z_{\mathrm{ref}}-d}{z_0}-\psi_m(z_{\mathrm{ref}}/L)}\right]^2.
   \]
3. If reporting a single drag coefficient for averaged multi-level speeds, report it at \(z_g\) (or explicitly at \(z_{\mathrm{ref}}\)), not at \(\bar{z}\).
4. Avoid using data within the roughness sublayer (~first 2–3 \(z_0\)); ensure stationarity and neutral filtering when invoking the neutral form.

## 8. Stability Function via Polylogarithm Formulation

We consider a stability modifier
\[
\phi\!\left(\frac{z}{L}\right)=\exp\!\Big(\alpha \,\mathrm{Li}_{1}\big(\beta\,\tfrac{z}{L}\big)\Big),
\]
where \(\mathrm{Li}_{1}(x)=\sum_{k=1}^{\infty}\frac{x^{k}}{k}=-\ln(1-x)\) (polylog of order 1). Avoid using the symbol \(s\) (reserved elsewhere); the polylog order here is fixed at 1.

Since \(\mathrm{Li}_1(x)=-\ln(1-x)\),
\[
\phi\!\left(\tfrac{z}{L}\right)=\exp\!\Big(\alpha\,(-\ln(1-\beta z/L))\Big)=(1-\beta z/L)^{-\alpha}.
\]

Domain constraint: require \(|\beta z/L|<1\) to stay away from the singularity at \(z = L/\beta\).

Neutral limit (\(z/L\to 0\)):
\[
\phi\left(\tfrac{z}{L}\right)\to 1.
\]

Series expansion (small \(|\beta z/L|\)):
\[
\phi=1+\alpha\beta \tfrac{z}{L}+\frac{\alpha(\alpha+1)}{2}(\beta\tfrac{z}{L})^{2}+O\big((z/L)^3\big).
\]

Parameter interpretation:
- \(\alpha\): controls curvature (strength of stability correction).
- \(\beta\): sets effective scaling of \(z/L\) relative to singular layer depth.
- Sign choices: For unstable \(L<0\), typically choose \(\alpha>0,\beta>0\) so \(\phi<1\) aloft (enhanced mixing); for stable \(L>0\), \(\alpha>0,\beta>0\) yields \(\phi>1\) (suppressed turbulent transport).

Connection to classical forms:
- Businger–Dyer style \(\phi_m(\zeta)=(1-c\zeta)^{-p}\) corresponds to \(\alpha=p\), \(\beta=c\).
- The polylog expression is a compact exponential/log representation offering analytic series control.

Mixing length or eddy viscosity modification:
\[
K_m(z)=K_{m0}(z)\, \phi^{-1}\!\left(\tfrac{z}{L}\right) = K_{m0}(z)\,(1-\beta z/L)^{\alpha}.
\]
Choose inverse or direct usage depending on whether \(\phi\) multiplies gradient terms or flux-profile corrections.

Practical estimation workflow:
1. Fit observed \(\phi(z/L)\) (from flux-gradient pairs) to \((1-\beta z/L)^{-\alpha}\).
2. Use nonlinear least squares; impose \(|\beta z/L|<1\) for all retained data.
3. Compare fitted \(\alpha,\beta\) to canonical stability constants.
4. For composite layers, allow piecewise \(\beta\) (surface vs. outer layer).

Bias caution:
- Using arithmetic averaging on \(z\) before forming \(z/L\) alters \(\phi\) because it is convex in \(z\).
- Evaluate \(\phi\) at each level then average; equivalently use geometric mean of \((1-\beta z/L)\) if compressing levels:
\[
\overline{\phi} = \exp\Big(\alpha\, \overline{\mathrm{Li}_1(\beta z/L)}\Big).
\]

Extension note:
- Higher-order \(\mathrm{Li}_{p}\) (with \(p>1\)) would introduce polylog sums beyond \(-\ln(1-x)\); current interest restricts to \(p=1\) for interpretability and direct mapping to power-law forms.

Summary:
\[
\phi(z/L)=(1-\beta z/L)^{-\alpha}
\]
gives a tunable, analytically tractable stability correction consistent with classical similarity, with clear parameter roles and controlled expansion.

## 9. Analytic Continuation and Asymptotics of \(\phi(z/L)=(1-\beta z/L)^{-\alpha}\)

Analytic continuation: write
\[
\phi\!\left(\tfrac{z}{L}\right)=\exp\!\Big(\alpha\,\mathrm{Li}_{1}(\beta z/L)\Big)
=\exp\!\Big(-\alpha \log(1-\beta z/L)\Big),
\]
where \(\log\) is the complex logarithm. Define principal branch with cut along \(\{1-\beta z/L \in (-\infty,0]\}\) i.e. a ray starting at \(z = L/\beta\) and extending so that \(\beta z/L \in [1,\infty)\) lies on the branch cut.

Branch / multi-valuedness:
\[
\log(1-\beta z/L) = \ln|1-\beta z/L| + i\arg(1-\beta z/L) + 2\pi i k,
\]
so
\[
\phi_k = (1-\beta z/L)^{-\alpha} e^{-2\pi i k \alpha},\quad k\in\mathbb{Z}.
\]
For real atmospheric applications use \(k=0\) and ensure \(1-\beta z/L>0\).

Local behavior near singularity: set \(z = L/\beta - \varepsilon\), \(|\varepsilon|\ll 1\):
\[
\phi \sim \varepsilon^{-\alpha}\left(1 + O(\varepsilon)\right),\qquad \text{blow-up if }\Re(\alpha)>0.
\]
If \(\Re(\alpha)<0\), \(\phi\to 0\) at the singular point (mathematically allowed, usually not physical).

Binomial expansion for small \(|\beta z/L|\):
\[
\phi = \sum_{n=0}^{\infty} \binom{\alpha + n -1}{n} (\beta z/L)^n
= 1+\alpha\beta\tfrac{z}{L}+\frac{\alpha(\alpha+1)}{2}(\beta\tfrac{z}{L})^2+\cdots.
\]

Asymptotic expansion for large \(|z/L|\) (with \(\beta z/L \to \infty\) off the branch cut):
\[
\phi = (1-\beta z/L)^{-\alpha} = (\beta z/L)^{-\alpha}\left(1 - \frac{1}{\beta z/L}\right)^{-\alpha}
= (\beta z/L)^{-\alpha}\sum_{n=0}^{\infty} \binom{-\alpha}{n}\left(-\frac{1}{\beta z/L}\right)^n,
\]
i.e.
\[
\phi \sim (\beta z/L)^{-\alpha}\Big[1 + \frac{\alpha}{\beta z/L} + \frac{\alpha(\alpha+1)}{2(\beta z/L)^2} + O((z/L)^{-3})\Big].
\]
So for large heights (or small \(|L|\)) \(\phi\) decays algebraically if \(\Re(\alpha)>0\).

Logarithmic form for differentiation:
\[
\log \phi = -\alpha \log(1-\beta z/L),
\]
parameter derivatives:
\[
\frac{\partial \phi}{\partial \alpha} = -\log(1-\beta z/L)\,\phi,\qquad
\frac{\partial \phi}{\partial \beta} = \frac{\alpha z/L}{1-\beta z/L}\,\phi.
\]
Sensitivity grows near the singularity as \(\sim (1-\beta z/L)^{-1}\).

Continuation via polylog identities: since \(\mathrm{Li}_1(x)=-\ln(1-x)\), higher polylog orders would introduce series
\[
\mathrm{Li}_p(x)=\sum_{k=1}^{\infty}\frac{x^k}{k^p},
\]
with branch point at \(x=1\); current \(p=1\) case inherits only the single logarithmic branch point—simpler analytic structure.

Atmospheric constraint: keep \(\beta z/L < 1\) (stable: \(z/L>0\), choose \(\beta\) small; unstable: \(L<0\) moves singularity to negative height, safely out of physical domain). Continuation beyond that domain is mathematical; physical models should restrict data so \(1-\beta z/L>0\) to avoid non-real \(\phi\).

Composite matching: use inner (small \(z/L\)) series and outer (large \(z/L\)) asymptotic; match in intermediate zone to build a uniform approximation if needed for wide dynamic ranges.

Summary:
- Analytic continuation controlled by complex log branch.
- Singular point at \(z=L/\beta\) governs blow-up/decay.
- Two practical expansions: small \(|\beta z/L|\) (power series) and large \(|z/L|\) (inverse power).
- Parameter sensitivity explicit via derivative formulas.

## 10. Stability / Shear Functions and Bulk Richardson Number Bias

Terminology:
- Stability modifier (stability function) \(\phi(z/L)\) as in Section 8.
- Shear function: expresses how mean shear (or eddy diffusivity) scales with a Richardson number.
- Bulk Richardson number between two levels captures buoyancy vs. shear production.

Bulk Richardson number between levels \(z_1<z_2\):
\[
Ri_{1,2} = \frac{g}{\bar{\theta}_v}\frac{\theta_{v}(z_2)-\theta_{v}(z_1)}{(U(z_2)-U(z_1))^2}(z_2 - z_1).
\]
Log‑law (with displacement \(d\), stability correction \(\psi_m\)):
\[
U(z)=\frac{u_*}{\kappa}\Big[\ln\frac{z-d}{z_0}-\psi_m(z/L)\Big].
\]
Then
\[
U(z_2)-U(z_1)=\frac{u_*}{\kappa}\Big[\ln\frac{z_2-d}{z_1-d}-\Delta\psi_m\Big],\quad \Delta\psi_m=\psi_m(z_2/L)-\psi_m(z_1/L).
\]
Substitute:
\[
Ri_{1,2} = \frac{g}{\bar{\theta}_v}\big(\Delta\theta_v\big)(z_2-z_1)\left(\frac{\kappa}{u_*}\right)^2\frac{1}{\Big[\ln\frac{z_2-d}{z_1-d}-\Delta\psi_m\Big]^2}.
\]

Bottom (surface–first level) bulk Richardson number (\(Ri_{1/2}\), surface treated as \(U(d+z_0)=0\)):
\[
Ri_{1/2} = \frac{g}{\bar{\theta}_v}\frac{\theta_v(z_2)-\theta_v(d+z_0)}{U(z_2)^2} z_2
= \frac{g}{\bar{\theta}_v}(\Delta\theta_v) z_2 \left(\frac{\kappa}{u_*}\right)^2 \frac{1}{\Big[\ln\frac{z_2-d}{z_0}-\psi_m(z_2/L)\Big]^2}.
\]
Using drag coefficient \(C_D(z_2)=\left[\frac{\kappa}{\ln\frac{z_2-d}{z_0}-\psi_m(z_2/L)}\right]^2\):
\[
Ri_{1/2} = \frac{g}{\bar{\theta}_v}(\Delta\theta_v) z_2 \frac{C_D(z_2)}{u_*^2}.
\]

Roughness / drag sensitivity:
- Misestimated \(z_0\) shifts the log term ⇒ multiplicative bias in \(Ri\) via squared inverse.
- Relative bias (two-level):
\[
\frac{Ri^{(\text{est})}_{1,2}}{Ri^{(\text{true})}_{1,2}}
= \left(\frac{\ln\frac{z_2-d}{z_1-d}-\Delta\psi_m^{(\text{true})}}{\ln\frac{z_2-d}{z_1-d}-\Delta\psi_m^{(\text{est})}}\right)^2.
\]
If stability neglected (\(\Delta\psi_m^{(\text{est})}=0\)):
\[
\frac{Ri^{(\text{est})}_{1,2}}{Ri^{(\text{true})}_{1,2}} = \left(\frac{\ln\frac{z_2-d}{z_1-d}-\Delta\psi_m}{\ln\frac{z_2-d}{z_1-d}}\right)^2.
\]

Shear function from gradient Richardson number:
Gradient Ri:
\[
Ri_g=\frac{g}{\theta_v}\frac{d\theta_v/dz}{(dU/dz)^2},\quad dU/dz=\frac{u_*}{\kappa(z-d)}\phi_m^{-1}(z/L).
\]
Hence
\[
Ri_g = \frac{g}{\theta_v}\frac{d\theta_v/dz}{\left(\frac{u_*}{\kappa(z-d)}\right)^2}\phi_m^{2}(z/L).
\]
A shear function \(S(Ri_g)\) can be defined (model choice). With \(\phi\) polylog form:
\[
\phi_m(z/L)=(1-\beta z/L)^{-\alpha} \Rightarrow Ri_g \propto (1-\beta z/L)^{-2\alpha}.
\]
So mapping \(z/L \mapsto Ri_g\) invertible (off singularity):
\[
(1-\beta z/L)= Ri_g^{-1/(2\alpha)} \times \text{(prefactor)}.
\]

Geometric mean impact:
- Averaging velocities first (log structure) ⇒ representative height \(z_g\); use \(z_g\) in log terms when forming bulk Ri from aggregated multi-level means to avoid denominator distortion.

Practical steps for unbiased \(Ri_{1/2}\):
1. Fit \(u_*, z_0\) with stability corrections.
2. Compute \(C_D(z_2)\), then \(Ri_{1/2}\) via drag form.
3. Report uncertainty by propagating errors in \(u_*\), \(z_0\), and \(\psi_m\) (log term squared ⇒ relative variance doubles that of the log term).
4. Avoid using arithmetic mean heights in denominators; prefer level-resolved calculation or geometric consolidation.

Key sensitivities:
- \(Ri_{1/2} \sim C_D/u_*^2\): overestimating \(u_*\) (due to low-biased \(z_0\)) suppresses \(Ri\) quadratically.
- Stability omission typically underestimates denominator ⇒ overestimates \(Ri\) (false classification toward stable).

Summary:
Surface roughness and drag errors propagate quadratically into bulk Richardson number estimates; consistent use of the log-profile (with \(\phi\)) and geometric mean principles reduces structural bias in \(Ri_{1/2}\) and multi-level \(Ri_{1,2}\).

## 11. Near-Neutral Upper Layers (|z/L| ≈ 0): Shear and Richardson Estimation

Assumptions:
- Near-neutral: \(|z/L| \to 0 \Rightarrow \psi_m \approx 0,\ \phi_m \approx 1\).
- Upper levels: use indices \(i>H\) (heights safely above roughness sublayer and local obstacles).
- Displacement height \(d\) known/estimated; use \(z' = z-d\).

Log-law:
\[
U(z)=\frac{u_*}{\kappa}\ln\frac{z'}{z_0}.
\]

Estimate friction velocity from upper levels:
- Fit \(U_i\) vs \(\ln z'_i\) for \(i>H\): slope \(A=\frac{u_*}{\kappa}\Rightarrow u_*=\kappa A\), intercept gives \(z_0\).
- Two-point estimate (i,j): \(u_*=\kappa\,\dfrac{U_j-U_i}{\ln(z'_j/z'_i)}\) at representative height \(z_g'=\sqrt{z'_i z'_j}\) (so \(z_g=d+z_g'\)).

Shear (analytic and discrete):
\[
\frac{dU}{dz}=\frac{u_*}{\kappa\,z'},\quad \text{so at } z_g:\ \left.\frac{dU}{dz}\right|_{z_g} \approx \frac{u_*}{\kappa\,z_g'}.
\]
Central-difference consistent with log-law:
\[
\left.\frac{dU}{dz}\right|_{z_g}\approx \frac{U_j-U_i}{z_j-z_i}
= \frac{u_*}{\kappa}\,\frac{\ln(z'_j/z'_i)}{z_j-z_i}
\approx \frac{u_*}{\kappa\,z_g'}\quad(\text{since } \ln\text{ is locally linear in }\ln z').
\]

Gradient Richardson number (near-neutral):
\[
Ri_g(z)\equiv \frac{g}{\theta_v}\frac{d\theta_v/dz}{(dU/dz)^2}
\approx \frac{g}{\theta_v}\left(\frac{d\theta_v}{dz}\right)\left(\frac{\kappa\,z'}{u_*}\right)^2.
\]
Discrete at \(z_g\) using central differences:
\[
Ri_g(z_g)\approx \frac{g}{\bar{\theta}_v}\,\frac{\Delta\theta_v}{z_j-z_i}
\left(\frac{\kappa\,z_g'}{u_*}\right)^2,\quad
z_g'=\sqrt{z'_i z'_j}.
\]

Bulk Richardson number between two upper levels (near-neutral):
\[
Ri_{i,j}=\frac{g}{\bar{\theta}_v}\frac{\theta_v(z_j)-\theta_v(z_i)}{(U_j-U_i)^2}(z_j-z_i)
= \frac{g}{\bar{\theta}_v}\,\Delta\theta_v\,(z_j-z_i)
\left(\frac{\kappa}{u_*}\right)^2
\frac{1}{\left[\ln\!\frac{z'_j}{z'_i}\right]^2}.
\]
Surface–level (near-neutral) special case:
\[
Ri_{i/2}=\frac{g}{\bar{\theta}_v}\,\Delta\theta_v\, z_i
\left(\frac{\kappa}{u_*}\right)^2
\frac{1}{\left[\ln\!\frac{z'_i}{z_0}\right]^2}.
\]

Workflow (near-neutral, upper levels z_i>H):
1. Filter data with \(|z/L|<\varepsilon\) and QC upper levels.
2. Regress \(U\) on \(\ln z'\) for \(i>H\) to obtain \(u_*\) and \(z_0\).
3. Compute shear at each level: \(dU/dz \approx u_*/(\kappa z')\); for pairs use \(z_g'\).
4. Compute \(Ri_g\) at \(z_g\) using measured temperature gradient; compute \(Ri_{i,j}\) with the log-law denominator.
5. Report uncertainties from regression (u*, z0) into shear and Ri; avoid using arithmetic mean heights—use \(z_g\).

Cautions:
- Exclude data within roughness sublayer (~2–3 \(z_0\)).
- If \(\Delta\theta_v\) is noisy near-neutral, prefer layer-averaged gradients or longer averaging to stabilize \(Ri\).
- If sonic-derived \(u_*\) is available, use it; the formulas above remain applicable with that \(u_*\).

## 12. Appendix: Reflections on \(\kappa\), \(\gamma\), and Notation

Historical values:
- Classical “consensus” \(\kappa \approx 0.40\pm 0.01\).
- Businger–Dyer formulations often used \(\kappa \approx 0.38\), emerging from early micrometeorological datasets (instrument tilt, flow distortion, limited Reynolds number).
- Modern high-Re boundary layer and channel/pipe experiments cluster near \(0.39\text{–}0.41\).

Relation to Euler–Mascheroni constant:
- Euler’s constant \(\gamma \approx 0.57721\); status: irrationality and transcendence remain unproven.
- Numerical coincidence: \(1-\gamma \approx 0.42278\) sits near the empirical range of \(\kappa\); \(1/\gamma \approx 1.732\) is not relevant.
- No accepted derivation linking \(\kappa\) to a simple function of \(\gamma\); proximity of \(1-\gamma\) is viewed as incidental.

Digamma function vs. ABL stability function:
- Mathematical digamma: \(\psi(x) = \frac{d}{dx}\ln\Gamma(x)\).
- Boundary-layer stability corrections also traditionally denoted \(\psi_m(z/L), \psi_h(z/L)\), causing confusion with \(\psi(x)\) in special-function contexts.
- In this document \(\phi(z/L)\) / \(\psi_m\) are atmospheric; digamma is explicitly “digamma” or \(\psi(\cdot)\) when needed in gamma-function derivations.

Estimation reflections:
- Library work on digamma/gamma identities (e.g., channel-flow integrals yielding logarithmic velocity profiles) can motivate indirect \(\kappa\) estimation by fitting the mean shear profile to forms involving \(\psi\) differences, but atmospheric practice favors direct regression \(U\) vs. \(\ln z\).
- Neutral, high-Re surface-layer data with careful tilt correction and displacement height treatment reduce spread in \(\kappa\).

Reasons for spread (0.38 vs 0.40):
- Sensor alignment and flow distortion.
- Incomplete exclusion of non-neutral stratification.
- Roughness sublayer contamination.
- Limited averaging times (non-stationarity).
- Displacement height misestimation shifting slope.

Notation discipline:
- Reserve \(\gamma\) for Euler–Mascheroni constant, avoid reusing for turbulence parameters.
- Use \(\kappa\) solely for von Kármán; atmospheric \(\psi_m\) kept distinct from digamma \(\psi(x)\).

Outlook:
- A joint publication (planned with Richard T. “Dick” McNider and Arastoo P. Biazar) could include a methodological appendix: comparative fits of \(\kappa\) using (i) classical log regression, (ii) stability-filtered subsets, (iii) special-function (digamma-based) analytic forms for channel/ABL synthesis.

Summary points:
- \(\kappa\) remains empirical; no closed-form proof in terms of \(\gamma\).
- Coincidence with \(1-\gamma\) is numerically interesting but not theoretically established.
- Clear separation of symbols reduces interpretive errors in mixed atmospheric–special-function work.

## 13. Where the Hasse–Stirling Framework Helps (ABL)

- Polylog/log expansions: \(\phi(z/L)=(1-\beta z/L)^{-\alpha}=\exp(\alpha\,\mathrm{Li}_1(\beta z/L))\). HS provides systematic expansions for \(\log\) and \(\mathrm{Li}_p\) based series with:
  - Truncation/error control via HS coefficient growth bounds.
  - Recurrence-driven, cacheable coefficients for rapid sweeps across many levels.
- Uniform asymptotics and continuation: The HS machinery cleanly handles the logarithmic branch structure (Sec. 9), enabling
  - Inner (small \(|z/L|\)) power series and outer (large \(|z/L|\)) inverse-power expansions.
  - Matched, uniform formulas with quantified remainder—useful when \(z/L\) spans decades.
- Bias corrections from averaging: HS finite-difference identities turn
  \[
  \overline{U}=\frac{1}{N}\sum U(z_i)
  \]
  into log-sum transforms, yielding compact, higher-order corrections when compressing multi-level data to a representative height (beyond the geometric-mean leading term).
- Drag and Richardson sensitivity: HS-generated series for
  \[
  C_D=\Big[\kappa/(\ln(\cdot)-\psi_m)\Big]^2,\quad Ri\propto (\ln(\cdot)-\psi_m)^{-2}
  \]
  produce analytic sensitivity maps and fast Jacobians for parameter estimation (\(z_0,d,\alpha,\beta\)).
- Special-function backbone: Where digamma/log-gamma enter statistical or inverse problems (e.g., priors/likelihoods on roughness/scale), HS offers accelerated, stable evaluation of \(\psi,\Gamma\), and related constants with explicit error bounds.

Practical takeaway:
- Use HS tables/recurrences to precompute φ-expansion coefficients and error bounds once per stability regime; reuse across profiles, bulk \(Ri\), and \(C_D\) evaluations.

