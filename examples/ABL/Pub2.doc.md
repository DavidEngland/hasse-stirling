# **STABILITY FUNCTIONS BASED UPON SHEAR FUNCTIONS**

DAVID E. ENGLAND AND RICHARD T. MCNIDER  
*Mathematical Sciences Department, University of Alabama in Huntsville, Huntsville, Alabama*

**Abstract.**  The stability functions for momentum and heat under a Richardson number formulation are derived from the nondimensional shear functions under a Monin-Obukhov formulation.  The Prandtl number is also derived as a function of the Richardson number.  Previously, this has been done only in a limited sense.  Because the Richardson number formulation is expressed in closed form, iterative techniques are no longer needed in numerical models that use Monin-Obukhov similarity theory.  This time-saving approach is made possible by deriving expressions for the friction velocity and temperature in terms of the Richardson number dependent stability functions.  In addition, the Richardson number approximation in the lowest layer is made to depend explicitly upon the surface roughness.


# **1\.  Introduction**

Under first-order closure the exchange coefficients for momentum (*Km*) and heat (*Kh*) depend upon the stability of the atmosphere, height above the surface (mixing length) and vertical wind shear.  Similarity theory yields shear functions, which depend upon the dimensionless Monin-Obukhov height (*z*) for incorporating stability.  The use of shear functions is widespread among boundary layer analysts, and numerous field programs have been conducted to determine these functions (see *e.g.*, Dyer and Hicks, 1970; Webb, 1970; Businger *et al*., 1971; Carl *et al*., 1973; Dyer, 1974; Hicks, 1976; Dyer and Bradley, 1982; Högström, 1985). 

	The existence of limit-cycle mixing is known to depend upon the turbulent Prandtl number *Pr* (Mahrt, 1989), which can be expressed in terms of shear functions.  Bendixson’s criterion can be applied to a two-layer, *K*\-closure model to determine the possible existence of limit-cycles (see England and McNider, 1994).  However, the derivatives needed in Bendixson’s criterion cannot be resolved analytically, because *z* depends upon the shear functions.  Such a circular definition also requires numerical boundary-layer models to use iterative solution procedures.  A closed-form method for incorporating stability dependence into the exchange coefficients would therefore be desirable.  The use of stability functions depending on the Richardson number (*Ri*) provides such a method.  Relationships between the shear and stability functions, as well as *z* and *Ri,* are known (see *e.g.*, Dyer, 1974; Paulson, 1970; Blackadar, 1979; Garratt, 1992).  To date, little work has been done in expressing *Pr* as a function of *Ri*.  The main goal of this study is to use Monin-Obukhov similarity theory to derive both the stability functions and *Pr*  in terms of *Ri*.  

	Prevalent choices for the shear functions have different forms for the stable boundary layer (SBL) and the unstable boundary layer (UBL).  Hence, derivations for the different regimes must be carried out separately.  The friction velocity and temperature will also be expressed in terms of stability functions and *Ri*, with explicit dependence upon surface roughness obtained through a logarithmic transformation.  In addition, it will be shown that if *Pr* \= 1 in the SBL, the stability functions are the same and have a quadratic form rather than the linear form introduced by Blackadar (1979).  This result is important because more modern and accurate experiments indicate that *Pr* does not significantly deviate from 1.00 in the SBL (see Yaglom, 1977; Högström, 1988; Kaimal and Finnigan, 1994).  The quadratic stability function has the advantage of having a continuous derivative in the SBL, which should provide smoother solutions of first-order closure models.  Finally, some mesoscale models diminish smoothness in the vertical direction by using a time-consuming, iterative *z* formulation near the surface and an inconsistent *Ri* formulation for the upper levels.  The inconsistency can be eliminated by using the results outlined in this work.

# **2\.  Exchange Coefficients**

The shear- and stability-function techniques for expressing the exchange coefficients differ only in whether atmospheric stability is parameterized by *z* or *Ri.*  The shear functions are based upon similarity theory, but, certain constants must be determined from experiments.  Similarity theory is used extensively in numerical models, especially near the ground, because a fine grid resolution is needed to resolve flux quantities.  A drawback of this formulation, from which the *Ri* formulation does not suffer, is that *z* must be found by an iterative procedure.  These two formulations are compared and contrasted in the following discussion.  

## 2.1.  MONIN-OBUKHOV FORMULATION

The exchange coefficients for momentum and heat expressed in terms of shear functions are
\[
K_m \;=\; \frac{\kappa\,u_*\,z}{\phi_m(\zeta)} \tag{1a}
\]
\[
K_h \;=\; \frac{\kappa\,u_*\,z}{\phi_h(\zeta)} \tag{1b}
\]
where the friction velocity is given by the gradient form
\[
u_* \;=\; \frac{\kappa\,z}{\phi_m(\zeta)}\,\frac{\partial U}{\partial z} \;,\quad
\zeta \equiv \frac{z}{L} \tag{2}
\]
the vertical wind shear by
\[
\frac{\partial U}{\partial z} \;=\; \frac{u_*}{\kappa\,z}\,\phi_m(\zeta) \tag{3}
\]
and the mixing length in the surface layer by
\[
\ell \;=\; \kappa\,z \tag{4}
\]
where \(\kappa\) is von Kármán’s constant, and \(z\) is height above the surface.  This investigation is restricted to shear functions of the following forms

## 2. Monin–Obukhov Similarity Theory (MOST): Essentials

### 2.1 Core scales and fluxes
- Friction velocity and temperature (scalar) scales
\[
u_*=\sqrt{-\overline{u'w'}},\qquad \theta_*=-\frac{\overline{w'\theta'}}{u_*},\qquad q_*=-\frac{\overline{w' q'}}{u_*}.
\]
- Obukhov length (using virtual potential temperature θ_v):
\[
L=-\frac{u_*^3\,\theta_v}{\kappa\,g\,\overline{w'\theta_v'}}.
\]
- Dimensionless height: \(\zeta=z/L\).

### 2.2 Flux–gradient (φ) relations
For momentum, heat (and scalars):
\[
\frac{\partial U}{\partial z}=\frac{u_*}{\kappa z}\,\phi_m(\zeta),\qquad
\frac{\partial \theta}{\partial z}=\frac{\theta_*}{\kappa z}\,\phi_h(\zeta),\qquad
\frac{\partial q}{\partial z}=\frac{q_*}{\kappa z}\,\phi_q(\zeta).
\]
K-theory (eddy diffusivities):
\[
K_m=\frac{u_* \kappa z}{\phi_m},\qquad K_h=\frac{u_* \kappa z}{\phi_h},\qquad Pr_t=\frac{K_m}{K_h}=\frac{\phi_h}{\phi_m}.
\]

### 2.3 Integrated profiles with ψ corrections (roughness/displacement)
Let displacement height d, momentum and heat roughness \(z_0,z_{0h}\), and \(\zeta=\frac{z-d}{L}\), \(\zeta_0=\frac{z_0}{L}\), \(\zeta_{0h}=\frac{z_{0h}}{L}\). Then
\[
U(z)=\frac{u_*}{\kappa}\Big[\ln\frac{z-d}{z_0}-\psi_m(\zeta)+\psi_m(\zeta_0)\Big],
\]
\[
\theta(z)-\theta_s=\frac{\theta_*}{\kappa}\Big[\ln\frac{z-d}{z_{0h}}-\psi_h(\zeta)+\psi_h(\zeta_{0h})\Big].
\]
Neutral limit: \(\psi_m=\psi_h=0,\ \phi_m=\phi_h=1\).

### 2.4 Canonical φ and ψ choices

Unstable (\(\zeta<0\), Businger–Dyer/Paulson):
\[
\phi_m=(1-16\zeta)^{-1/4},\quad \phi_h=(1-16\zeta)^{-1/2},\quad x=(1-16\zeta)^{1/4},
\]
\[
\psi_m=2\ln\frac{1+x}{2}+\ln\frac{1+x^2}{2}-2\arctan x+\frac{\pi}{2},\quad
\psi_h=2\ln\frac{1+x^2}{2}.
\]

Stable (\(\zeta>0\), common linear/quadratic forms; Högström-style linear shown):
\[
\phi_m=1+a_m \zeta,\quad \phi_h=1+a_h \zeta,\quad \psi_m=\psi_h=-b\,\zeta,\ \ (a_m\!\approx\!a_h\!\approx\!5,\ b\!\approx\!5).
\]
Notes: modern datasets may support gentle curvature (quadratic) in very stable layers; guard domains where \(1-\beta\zeta>0\) for power-law fits.

### 2.5 Bulk coefficients (10-m style)
At reference height \(z_r\):
\[
C_D(z_r)=\Bigg[\frac{\kappa}{\ln\frac{z_r-d}{z_0}-\psi_m(\zeta_r)+\psi_m(\zeta_0)}\Bigg]^2,\quad
C_H(z_r)=\frac{\kappa^2}{\big[\ln\frac{z_r-d}{z_0}-\psi_m\big]\big[\ln\frac{z_r-d}{z_{0h}}-\psi_h\big]}.
\]

### 2.6 Practical considerations
- Roughness lengths: \(z_{0h}\le z_0\), often parameterized via roughness Reynolds or a fixed ratio over land/sea.
- Displacement height: use \(z' = z-d\) consistently (and in geometric means if compressing levels).
- Near-surface masking: avoid roughness sublayer (≈ first 2–3 \(z_0\)).
- Domain guards: unstable \(1-16\zeta>0\); power-law \((1-\beta\zeta)^{-\alpha}\) requires \(1-\beta\zeta>0\).

## 3. MOST forms used in this work (for mapping to Ri later)
We employ power-law stability functions consistent with the polylog view:
\[
\phi_m(\zeta)=(1-\beta_m\zeta)^{-\alpha_m},\qquad \phi_h(\zeta)=(1-\beta_h\zeta)^{-\alpha_h},
\]
with corresponding ψ via analytic integration, and neutral/limit checks as in §2.4.

## Appendix: Locating a Clean Preprint (for archival/reproduction)
- Search identifiers: title “Stability Functions based upon Shear Functions” (1995), authors “England; McNider”; journal “Boundary-Layer Meteorology”.
- Check: personal storage (old Mac “.doc”/“.wpd”), ZIP backups, and email archives around 1994–1996.
- Institutional repositories: UAH Huntsville, author pages (McNider), departmental tech reports.
- Indexers: Google Scholar, SpringerLink (journal site), ResearchGate, Semantic Scholar; look for “preprint”, “accepted manuscript”, or “postprint”.
- If only scanned PDF exists: run OCR (math-aware), then replace images with LaTeX using the equations above; verify against printed pagination.