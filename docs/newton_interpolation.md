# 📌 Newton Interpolation (Divided Differences)

## 🔹 Overview

This Newton’s interpolation method constructs polynomials incrementally using **divided differences**. It is particularly useful when new data points are added dynamically.

## 🎯 When to Use?

-   **Unevenly spaced data points** (handles irregular data well).
-   When you need to **incrementally add more points** without recalculating everything from scratch.

## ⚡ Advantages

✔ Efficient for large datasets with new points.  
✔ Works well with **unevenly spaced** data points.

## 📖 Formula

Newton’s interpolation polynomial:

\[
P(x) = f(x_0) + f[x_0, x_1] (x - x_0) + f[x_0, x_1, x_2] (x - x_0)(x - x_1) + ...
\]

where **`f[x_0, x_1]`, `f[x_0, x_1, x_2]`** are divided differences.

---

## 🎨 **Visualizing Newton's Divided Differences**

Consider **three points**:  
\[
(0, -1), (1, 1), (2, 4)
\]

We construct the **divided difference table**:

| \( x \) | \( f(x) \) | First Divided Difference \( f[x_i, x_{i+1}] \) | Second Divided Difference \( f[x_i, x_{i+1}, x_{i+2}] \) |
| ------- | ---------- | ---------------------------------------------- | -------------------------------------------------------- |
| 0       | -1         |                                                |                                                          |
|         |            | **\( P_0 = f(x_0) = -1 \)**                    |                                                          |
| 1       | 1          | **\( P_1 = \frac{1 - (-1)}{1-0} = 2 \)**       |                                                          |
|         |            |                                                | **\( P_2 = \frac{3 - 2}{2-0} = 0.5 \)**                  |
| 2       | 4          | **\( \frac{4 - 1}{2-1} = 3 \)**                |                                                          |

Using these values, we get the polynomial:

\[
P(x) = P_0 + P_1(x - x_0) + P_2(x - x_0)(x - x_1)
\]

Substituting the values:

\[
P(x) = -1 + 2(x - 0) + 0.5(x - 0)(x - 1)
\]

This is the Newton interpolating polynomial for the given points.

---

## 🔎 **Key Takeaways**

✔ **Incremental Construction**: Each step refines the polynomial.  
✔ **Handles Uneven Spacing**: Unlike Lagrange, Newton’s method does not require equally spaced points.  
✔ **Efficient for Large Data**: You don’t need to recompute the whole polynomial when adding a new point.
