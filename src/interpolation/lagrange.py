# Simple hash cache for basis polynomials
_cache = {}

def lagrange_interpolation(points, x_approx):
    """Basic Lagrange interpolation - O(n²) every time"""
    n = len(points)
    result = 0
    
    for i in range(n):
        xi, yi = points[i]
        li = yi
        for j in range(n):
            if i != j:
                xj = points[j][0]
                li *= (x_approx - xj) / (xi - xj)
        result += li
    
    return result

def lagrange_with_hashing(points, x_approx):
    """Lagrange with simple hash caching - DSA optimization"""
    n = len(points)
    result = 0
    
    # Create cache key from points
    points_key = tuple(sorted(points))
    
    for i in range(n):
        xi, yi = points[i]
        
        # Check cache for basis polynomial
        cache_key = (points_key, i, x_approx)
        if cache_key in _cache:
            li = _cache[cache_key] * yi
        else:
            # Compute basis polynomial
            li = yi
            for j in range(n):
                if i != j:
                    xj = points[j][0]
                    li *= (x_approx - xj) / (xi - xj)
            # Cache the normalized basis value
            _cache[cache_key] = li / yi
        
        result += li
    
    return result

def clear_cache():
    """Clear the hash cache"""
    global _cache
    _cache.clear()
