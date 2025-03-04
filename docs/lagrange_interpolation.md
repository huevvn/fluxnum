# 📌 Lagrange Interpolation

## 🔹 Overview

Lagrange interpolation constructs a single polynomial that passes **exactly through a given set of points** using **Lagrange basis polynomials**.

## 🎯 When to Use?

-   **Small datasets** where you need a **single polynomial**.
-   When an **explicit formula** is required, rather than an incremental approach.

## ⚡ Advantages

✔ Provides a **single polynomial expression**.  
✔ Easy to understand and implement.

## 📖 Formula

Lagrange’s interpolation formula:

```math
P(x) = \sum_{i=0}^{n} f(x_i) L_i(x)
```
