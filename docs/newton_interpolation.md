# 📌 Newton Interpolation

## 🔹 Overview

Newton’s interpolation method constructs polynomials incrementally using **divided differences**. It is particularly useful when new data points are added dynamically.

## 🎯 When to Use?

-   **Unevenly spaced data points** (handles irregular data well).
-   When you need to **incrementally add more points** without recalculating everything from scratch.

## ⚡ Advantages

✔ Efficient for large datasets with new points.  
✔ Works well with **unevenly spaced** data points.

## 📖 Formula

Newton’s interpolation polynomial:

```math
P(x) = f(x_0) + f[x_0, x_1] (x - x_0) + f[x_0, x_1, x_2] (x - x_0)(x - x_1) + ...
```
