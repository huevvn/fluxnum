# Simple heap for storing residuals
import heapq

def least_squares_basic(points):
    """Basic least squares linear regression - brute force"""
    n = len(points)
    if n < 2:
        return 0, 0
    
    # Calculate sums
    sum_x = sum(p[0] for p in points)
    sum_y = sum(p[1] for p in points)
    sum_xy = sum(p[0] * p[1] for p in points)
    sum_x2 = sum(p[0] ** 2 for p in points)
    
    # Calculate slope and intercept
    slope = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x ** 2)
    intercept = (sum_y - slope * sum_x) / n
    
    return slope, intercept

def least_squares_with_heap(points):
    """Least squares with heap for finding top-K worst errors efficiently
    
    DSA Benefit: O(n log k) vs O(n log n) when k << n
    Real-world use: Quality control, outlier detection, data cleaning
    """
    slope, intercept = least_squares_basic(points)
    
    # Use heap to efficiently find worst errors without full sorting
    # This is useful when you only need top-K outliers from large datasets
    k = 3  # Only track top 3 worst errors
    worst_errors = []  # Min heap - keeps smallest of the "worst" errors
    
    for x, y in points:
        predicted = slope * x + intercept
        error = abs(y - predicted)
        
        if len(worst_errors) < k:
            heapq.heappush(worst_errors, error)  # Add if space available
        elif error > worst_errors[0]:  # If worse than best of worst
            heapq.heapreplace(worst_errors, error)  # Replace smallest worst
    
    # Convert to sorted list (worst first)
    final_errors = sorted(worst_errors, reverse=True)
    
    return slope, intercept, final_errors

def predict_linear(x, slope, intercept):
    """Predict y value using linear model"""
    return slope * x + intercept

def polynomial_regression(points, degree=2):
    """Simple polynomial regression using normal equations"""
    n = len(points)
    x_vals = [p[0] for p in points]
    y_vals = [p[1] for p in points]
    
    # Build matrix for normal equations (simplified for degree 2)
    if degree == 2:
        # For y = ax² + bx + c
        sum_x = sum(x_vals)
        sum_x2 = sum(x ** 2 for x in x_vals)
        sum_x3 = sum(x ** 3 for x in x_vals)
        sum_x4 = sum(x ** 4 for x in x_vals)
        sum_y = sum(y_vals)
        sum_xy = sum(x_vals[i] * y_vals[i] for i in range(n))
        sum_x2y = sum(x_vals[i] ** 2 * y_vals[i] for i in range(n))
        
        # Solve 3x3 system (simplified)
        # This is a basic implementation for demo
        a = (n * sum_x2y - sum_x2 * sum_y) / (n * sum_x4 - sum_x2 ** 2)
        b = (sum_xy - a * sum_x3) / sum_x2 if sum_x2 != 0 else 0
        c = (sum_y - a * sum_x2 - b * sum_x) / n
        
        return [c, b, a]  # coefficients for c + bx + ax²
    
    # Fallback to linear
    slope, intercept = least_squares_basic(points)
    return [intercept, slope]

def predict_polynomial(x, coefficients):
    """Predict using polynomial coefficients"""
    result = 0
    for i, coef in enumerate(coefficients):
        result += coef * (x ** i)
    return result
