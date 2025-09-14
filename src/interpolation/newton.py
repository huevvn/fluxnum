# Simple DP table cache
_dp_cache = {}

def newton_interpolation(points, x_approx):
    """Basic Newton interpolation - O(n²) every time"""
    x_vals, y_vals = zip(*points)
    n = len(points)
    
    # Build divided difference table
    coef = list(y_vals)
    for i in range(1, n):
        for j in range(n - 1, i - 1, -1):
            coef[j] = (coef[j] - coef[j - 1]) / (x_vals[j] - x_vals[j - i])
    
    # Evaluate polynomial
    result = coef[0]
    term = 1
    for i in range(1, n):
        term *= (x_approx - x_vals[i - 1])
        result += coef[i] * term
    
    return result

def newton_with_dp(points, x_approx):
    """Newton with simple DP caching - DSA optimization"""
    x_vals, y_vals = zip(*points)
    n = len(points)
    
    # Create cache key from points
    points_key = tuple(sorted(points))
    
    # Check if DP table is cached
    if points_key in _dp_cache:
        coef = _dp_cache[points_key]
    else:
        # Build divided difference table using DP
        coef = list(y_vals)
        for i in range(1, n):
            for j in range(n - 1, i - 1, -1):
                coef[j] = (coef[j] - coef[j - 1]) / (x_vals[j] - x_vals[j - i])
        # Cache the coefficients
        _dp_cache[points_key] = coef[:]
    
    # Evaluate polynomial
    result = coef[0]
    term = 1
    for i in range(1, n):
        term *= (x_approx - x_vals[i - 1])
        result += coef[i] * term
    
    return result

def clear_dp_cache():
    """Clear the DP cache"""
    global _dp_cache
    _dp_cache.clear()