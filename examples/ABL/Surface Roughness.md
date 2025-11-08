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

## 8. Stability Corrections (ψ) and Roughness for Heat
Stability-corrected integrated forms (with displacement d):
\[
U(z)=\frac{u_*}{\kappa}\Big[\ln\frac{z-d}{z_0}-\psi_m(z/L)\Big],\quad
\theta(z)-\theta_s=\frac{\theta_*}{\kappa}\Big[\ln\frac{z-d}{z_{0h}}-\psi_h(z/L)\Big].
\]
Canonical choices:
- Unstable (\(\zeta<0\)):
  \[
  \phi_m=(1-16\zeta)^{-1/4},\ \phi_h=(1-16\zeta)^{-1/2},\ x=(1-16\zeta)^{1/4},
  \]
  \[
  \psi_m=2\ln\frac{1+x}{2}+\ln\frac{1+x^2}{2}-2\arctan x+\frac{\pi}{2},\quad
  \psi_h=2\ln\frac{1+x^2}{2}.
  \]
- Stable (\(\zeta>0\)): \(\phi_{m,h}=1+5\zeta,\ \psi_{m,h}=-5\zeta\) (variants with mild curvature are used in very stable conditions).

Heat roughness \(z_{0h}\):
- Typically \(z_{0h}\le z_0\); over land often parameterized via roughness Reynolds or fixed \(z_{0h}/z_0\).
- Use separate \(\zeta_{0h}=z_{0h}/L\) in integrated temperature.

## 9. Bulk Transfer Coefficients with Stability
At reference height \(z_r\) (outside roughness sublayer):
\[
C_D(z_r)=\Bigg[\frac{\kappa}{\ln\frac{z_r-d}{z_0}-\psi_m(\zeta_r)}\Bigg]^2,\quad
C_H(z_r)=\frac{\kappa^2}{\big[\ln\frac{z_r-d}{z_0}-\psi_m(\zeta_r)\big]\big[\ln\frac{z_r-d}{z_{0h}}-\psi_h(\zeta_r)\big]}.
\]
Workflow: estimate \(u_*,z_0,z_{0h}\) by stability-aware regression; evaluate \(C_{D,H}\) at a specified \(z_r\) (or at \(z_g\) for averaged winds).

## 10. MOST Power-Law Variant (for modeling)
For analytic work (and series/continuation):
\[
\phi_m(\zeta)=(1-\beta_m\zeta)^{-\alpha_m},\quad \phi_h(\zeta)=(1-\beta_h\zeta)^{-\alpha_h},
\]
with domain \(1-\beta_{(\cdot)}\zeta>0\). Integrate to obtain \(\psi_{m,h}\) or use near-neutral series:
\[
\phi\simeq 1+\alpha\beta\,\zeta+\tfrac{1}{2}\alpha(\alpha+1)(\beta\zeta)^2+\cdots.
\]
Use guards near the singular approach (e.g., \(\zeta<0.7/\max\beta\)).

