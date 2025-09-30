# Relationship Between Generalized Stirling Number Notations

## Comparing Notation Systems

The literature on generalized Stirling numbers uses various notation systems. Here we clarify the relationship between two important ones:

1. **Hsu-Shiue Notation**: $S(n,k;\alpha,\beta,r)$
2. **Our Developed Notation**: $S_{m,n}(a,b)$

## Direct Correspondence

The relationship between these notations can be expressed as:

$$S_{m,n}(a,b) = S(m,n;a,b,0)$$

when the third parameter $r=0$ in the Hsu-Shiue framework.

## Recurrence Relations

The Hsu-Shiue numbers satisfy:

$$S(n,k;\alpha,\beta,r) = S(n-1,k-1;\alpha,\beta,r) + (\beta k - \alpha n + r)S(n-1,k;\alpha,\beta,r)$$

While our $S_{m,n}(a,b)$ numbers satisfy:

$$S_{m,n}(a,b) = S_{m-1,n-1}(a,b) + (bn - am)S_{m-1,n}(a,b)$$

We see that these match exactly when $r=0$.

## Extended Notation

To fully capture the Hsu-Shiue generalization with the $r$ parameter, we would need to extend our notation to something like $S_{m,n}(a,b,c)$ where:

$$S_{m,n}(a,b,c) = S_{m-1,n-1}(a,b,c) + (bn - am + c)S_{m-1,n}(a,b,c)$$

Then we would have:

$$S_{m,n}(a,b,c) = S(m,n;a,b,c)$$

## Special Cases in Our Framework

In our notation:

1. Classical Stirling numbers of the first kind: $s(n,k) = S_{n,k}(1,0)$
2. Classical Stirling numbers of the second kind: $S(n,k) = S_{n,k}(0,1)$
3. $r$-Stirling numbers of the second kind: $S_r(n,k) = S_{n,k}(0,1)$ with modified initial conditions
4. Whitney numbers of the first kind: $w_m(r,n) = S_{n,r}(-m,0)$
5. $r$-Lah numbers: $L_r(n,k) = S_{n,k}(-r,r)$

## Advantages of Different Notations

The Hsu-Shiue notation $S(n,k;\alpha,\beta,r)$ offers:
- Explicit parameter for the constant term ($r$)
- Widely recognized in the literature
- Clearer connection to classical Stirling numbers

Our notation $S_{m,n}(a,b)$ offers:
- More compact representation when $r=0$
- Easier subscript/superscript typesetting
- Consistent with notation used in our computational framework

## Significance of the Parameter r

The fifth parameter r in $S(n,k;\alpha,\beta,r)$ has substantial mathematical and combinatorial significance:

### 1. Mathematical Role

Mathematically, r serves as a constant term in the recurrence relation:

$$S(n,k;\alpha,\beta,r) = S(n-1,k-1;\alpha,\beta,r) + (\beta k - \alpha n + r)S(n-1,k;\alpha,\beta,r)$$

This constant shifts the weight between the two terms in the recurrence, allowing for a broader family of number sequences than the four-parameter version.

### 2. Combinatorial Interpretation

The parameter r can be interpreted as:

- A fixed offset in counting processes
- A constant weight applied to certain combinatorial structures
- A parameter controlling initial conditions in counting sequences

For example, in r-Stirling numbers of the second kind $S_r(n,k)$, the parameter r indicates that the first r elements must be placed in distinct subsets. This requirement modifies the counting process and yields a different sequence.

### 3. Connection to Classical Cases

Several important special cases are defined by specific values of r:

- Classical Stirling numbers: $S(n,k;0,1,0)$ and $S(n,k;1,0,0)$
- r-Stirling numbers: $S(n,k;0,1,r)$
- r-Lah numbers: $S(n,k;-r,r,0)$ (note that r appears in α and β but not in the 5th parameter)
- r-Whitney numbers: related to $S(n,k;-r,0,0)$

### 4. Impact on Hasse-Stirling Framework

In the Hasse-Stirling framework, the parameter r affects:

1. **Operator Behavior**: $\mathcal{H}_{\alpha,\beta,r}$ acts differently on functions depending on r
2. **Asymptotic Expansions**: The parameter r influences convergence rates and error terms
3. **Special Function Identities**: Different values of r yield different connections to special functions

For instance, the identity:

$$\mathcal{H}_{0,1,r}(x^{n-r}) = \sum_{k=r}^{n} S_r(n,k) \frac{B_{k-r}(x)}{(k-r)!}$$

shows how r directly affects the relationship between the Hasse operator and Bernoulli polynomials.

### 5. Application Examples

The r-parameter proves essential in several applications:

- **Quantum Physics**: Different r values correspond to different boundary conditions in quantum systems
- **Combinatorial Geometry**: r can represent dimensional shifts in counting problems
- **Network Theory**: In certain graph enumeration problems, r represents a fixed substructure requirement

As noted by Hsu and Shiue (1998), this fifth parameter completes the unified approach to generalized Stirling numbers, making the framework significantly more flexible and broadly applicable.

## Application in the Hasse-Stirling Framework

Within the Hasse-Stirling framework, we can use either notation:

$$\mathcal{H}_{\alpha,\beta,r}(f)(x) = \sum_{m=0}^{\infty} \sum_{n=0}^{m} H_{m,n}^{\alpha,\beta,r} f(x+n)$$

Or equivalently:

$$\mathcal{H}_{a,b,c}(f)(x) = \sum_{m=0}^{\infty} \sum_{n=0}^{m} H_{m,n}^{a,b,c} f(x+n)$$

Where the Hasse coefficients can be expressed in terms of either notation:

$$H_{m,n}^{\alpha,\beta,r} = \frac{1}{m+1} \sum_{j=0}^{n} (-1)^{n-j} \binom{n}{j} S(m,j;\alpha,\beta,r)$$

Or:

$$H_{m,n}^{a,b,c} = \frac{1}{m+1} \sum_{j=0}^{n} (-1)^{n-j} \binom{n}{j} S_{m,j}(a,b,c)$$

For our work focusing on cases where $r=0$ (or $c=0$), we can simplify to:

$$H_{m,n}^{a,b} = \frac{1}{m+1} \sum_{j=0}^{n} (-1)^{n-j} \binom{n}{j} S_{m,j}(a,b)$$
