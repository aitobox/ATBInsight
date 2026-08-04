# Relative Velocity and Closing Speed

## Summary
In physics simulations and game engines, it is frequently necessary to calculate how fast two objects are approaching or moving away from one another. This guide explores the concept of **closing speed**—defined as the normal component of the relative velocity between two objects—and breaks down how to compute it using vector projections and time-dependent calculus.

---

## 1. Relative Velocity and its Components

Suppose we have two point-like objects, $A$ and $B$, with velocity vectors $\vec{V}_A$ and $\vec{V}_B$. The **relative velocity** of $B$ with respect to $A$ is expressed as:

$$\vec{V}_{B|A} = \vec{V}_B - \vec{V}_A$$

In other words, this represents the velocity of $B$ within $A$'s frame of reference. 

Since relative velocity is a vector, we can decompose it into orthogonal components. By drawing a line connecting the two objects in a 2D (or 3D) space:
* **Normal Component:** The component of $\vec{V}_{B|A}$ aligned directly along the line connecting the two objects.
* **Tangential Component:** The component perpendicular to this connecting line.

---

## 2. Computing the Normal Component

To find the normal component, we utilize a **vector projection**. 

Let the positions of $A$ and $B$ be represented by position vectors $\vec{P}_A$ and $\vec{P}_B$. The line connecting them is given by the relative position vector $\vec{P}_B - \vec{P}_A$. 

Because we only need the *direction* of this line rather than its magnitude, we convert it into a **unit vector**:

$$\widehat{P} = \frac{\vec{P}_B - \vec{P}_A}{|\vec{P}_B - \vec{P}_A|}$$

To find the projection of $\vec{V}_{B|A}$ onto $\widehat{P}$, we compute the dot product:

$$S_c = \vec{V}_{B|A} \cdot \widehat{P} = (\vec{V}_B - \vec{V}_A) \cdot \widehat{P}$$

### Understanding Closing Speed ($S_c$)
The resulting quantity, $S_c$, is a scalar known as the **closing speed** (also referred to as *signed separation speed* or *normal relative speed*). It describes how rapidly the distance between the two objects is changing:
* **Positive ($S_c > 0$):** The objects are drifting farther apart.
* **Negative ($S_c < 0$):** The objects are getting closer together.

---

## 3. Examples

Let’s review how this works in practice through various scenarios:

* **Example I:**
  $$\widehat{P} = \frac{\langle 4, 0 \rangle}{|\langle 4, 0 \rangle|} = \langle 1, 0 \rangle$$
  $$S_c = \langle -3, 0 \rangle \cdot \langle 1, 0 \rangle = -3$$
  *Result:* The negative sign indicates the objects are approaching each other.

* **Example II:**
  $$S_c = \langle 3, 0 \rangle \cdot \langle 1, 0 \rangle = 3$$
  *Result:* Same magnitude as Example I, but positive because the objects are moving apart.

* **Example III (Object $B$ to the left of $A$):**
  $$\widehat{P} = \frac{\langle -2, 0 \rangle}{|\langle -2, 0 \rangle|} = \langle -1, 0 \rangle$$
  $$S_c = \langle 3, 0 \rangle \cdot \langle -1, 0 \rangle = -3$$
  *Result:* Yields consistent results even when positions are reversed, as both the unit vector and relative velocity directions flip.

* **Example IV (Arbitrary positions and velocities):**
  $$\widehat{P} = \frac{\langle 3, 4 \rangle}{|\langle 3, 4 \rangle|} = \langle 0.6, 0.8 \rangle$$
  $$S_c = \langle -3, -6 \rangle \cdot \langle 0.6, 0.8 \rangle = -6.6$$
  *Result:* Demonstrates instantaneous closing speed. Because positions change over time, $S_c$ is strictly time-dependent.

---

## 4. Closing Speed as a Function of Time

The calculations above offer an instantaneous, static snapshot. To view this dynamically, we can formulate closing speed using standard calculus.

Let the position vectors of $A$ and $B$ be functions of time, $\vec{P}_A(t)$ and $\vec{P}_B(t)$. The relative position vector is:

$$\vec{R}(t) = \vec{P}_B(t) - \vec{P}_A(t)$$

The scalar distance between them is the magnitude of this vector:

$$r(t) = |\vec{R}(t)| = |\vec{P}_B(t) - \vec{P}_A(t)| = \sqrt{x(t)^2 + y(t)^2}$$

We want to find $\frac{dr(t)}{dt}$, the rate of change of distance over time. Applying the chain rule:

$$\frac{dr(t)}{dt} = \frac{2x(t)x'(t) + 2y(t)y'(t)}{2\sqrt{x(t)^2 + y(t)^2}} = \frac{x(t)x'(t) + y(t)y'(t)}{\sqrt{x(t)^2 + y(t)^2}}$$

Rewriting this in vector notation, the numerator becomes the dot product of $\vec{R}(t)$ and its time derivative $\vec{R}'(t)$:

$$\frac{dr(t)}{dt} = \frac{\vec{R}(t) \cdot \vec{R}'(t)}{|\vec{R}(t)|} = \widehat{R}(t) \cdot \vec{R}'(t)$$

Since $\widehat{R}(t)$ is equivalent to our unit vector $\widehat{P}(t)$, and $\vec{R}'(t) = \vec{V}_B(t) - \vec{V}_A(t)$, we arrive at the final time-dependent formulation:

$$\frac{dr(t)}{dt} = \widehat{P}(t) \cdot \left(\vec{V}_B(t) - \vec{V}_A(t)\right)$$

---

## Footnotes

1. <span id="footnote-1"></span>Throughout this post, we assume our objects are sufficiently far apart that they can be treated as *points* (or *particles*) without any shape, area, or volume. [↩](#footnote-reference-1)
2. <span id="footnote-2"></span>The velocity components should be the same regardless of how far apart the two objects are. [↩](#footnote-reference-2)
3. <span id="footnote-3"></span>In the standard projection formula, we would also divide by the magnitude of $\widehat{P}$, but in our case, it is already a unit vector. [↩](#footnote-reference-3)
4. <span id="footnote-4"></span>Some online sources describe closing speed as "closing velocity" because it has a sign. However, scalars can be signed, and closing speed is fundamentally a scalar, not a vector. [↩](#footnote-reference-4)
5. <span id="footnote-5"></span>The notation $x'(t)$ denotes $\frac{dx(t)}{dt}$. [↩](#footnote-reference-5)