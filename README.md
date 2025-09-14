# Fluxnum ⚡️

A Clean Optimized Numerical Analysis Library - Python

## 🎯 Features

### Core Methods

-   **Lagrange Interpolation**
-   **Newton Interpolation**
-   **Least Squares Regression**

### DSA Optimizations Applied

1. **Simple Hashing** - Cache basis polynomials for repeated calculations
2. **Dynamic Programming** - Store divided difference tables to avoid recomputation
3. **Simple Heaps** - Track worst residuals in regression analysis

## 🚀 Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Run the application
python src/run.py

# Run benchmarks
python src/benchmark.py
```

## 📊 Performance Comparison

**Test Setup:** 10 data points, 9 evaluation points, 50 iterations each method

Results from actual benchmark (`python src/benchmark.py`):

| Method     | Basic Time | DSA Time | Speedup | Technique           |
| ---------- | ---------- | -------- | ------- | ------------------- |
| Lagrange   | 0.005s     | 0.002s   | 2.6x    | Hash caching        |
| Newton     | 0.003s     | 0.001s   | 4.0x    | DP table storage    |
| Regression | 0.007s     | 0.010s   | 0.7x\*  | Heap error tracking |

\*Regression is slower due to heap overhead, but provides error analysis

**How tested:**

-   50 repeated runs of each algorithm for statistical accuracy
-   Same polynomial data: f(x) = x² + 2x + 1 with 10 points
-   Evaluation at 9 intermediate points (x + 0.5)
-   Measures pure computation time, not I/O or setup

## 🛠 Usage Examples

### Interpolation

```python
from interpolation.lagrange import lagrange_interpolation, lagrange_with_hashing

points = [(1, 2), (2, 5), (3, 10)]
x = 2.5

# Basic version
result1 = lagrange_interpolation(points, x)

# DSA optimized version
result2 = lagrange_with_hashing(points, x)
```

### Regression

```python
from interpolation.regression import least_squares_basic, least_squares_with_heap

points = [(1, 2), (2, 4), (3, 5), (4, 8)]

# Basic linear regression
slope, intercept = least_squares_basic(points)

# With heap tracking of worst errors
slope, intercept, errors = least_squares_with_heap(points)
```
```
