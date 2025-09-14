import time
from interpolation.lagrange import lagrange_interpolation, lagrange_with_hashing, clear_cache
from interpolation.newton import newton_interpolation, newton_with_dp, clear_dp_cache
from interpolation.regression import least_squares_basic, least_squares_with_heap

def benchmark_interpolation():
    """Simple benchmark: brute force vs DSA optimized"""
    print("🚀 FluxNum Simple Benchmark")
    print("=" * 40)
    
    # Test data - polynomial function f(x) = x² + 2x + 1
    points = [(i, i**2 + 2*i + 1) for i in range(10)]
    test_values = [i + 0.5 for i in range(9)]
    iterations = 50  # Number of test runs for accuracy
    
    print(f"Test Setup:")
    print(f"  Data: {len(points)} points from f(x) = x² + 2x + 1")
    print(f"  Evaluations: {len(test_values)} points")
    print(f"  Iterations: {iterations} runs each")
    print(f"  Points: {points[:3]}...{points[-1]}")
    
    # Lagrange benchmark
    print("\n📊 Lagrange Interpolation:")
    
    # Brute force - multiple runs for statistical accuracy
    start = time.perf_counter()
    for _ in range(iterations):
        for x in test_values:
            lagrange_interpolation(points, x)
    brute_time = time.perf_counter() - start
    
    # With hashing - clear cache first for fair comparison
    clear_cache()
    start = time.perf_counter()
    for _ in range(iterations):
        for x in test_values:
            lagrange_with_hashing(points, x)
    hash_time = time.perf_counter() - start
    
    print(f"  Brute force: {brute_time:.6f}s ({brute_time/iterations:.6f}s per run)")
    print(f"  With hashing: {hash_time:.6f}s ({hash_time/iterations:.6f}s per run)")
    print(f"  Speedup: {brute_time/hash_time:.2f}x")
    
    # Newton benchmark
    print("\n📊 Newton Interpolation:")
    
    # Brute force
    start = time.perf_counter()
    for _ in range(iterations):
        for x in test_values:
            newton_interpolation(points, x)
    brute_time = time.perf_counter() - start
    
    # With DP - clear cache first
    clear_dp_cache()
    start = time.perf_counter()
    for _ in range(iterations):
        for x in test_values:
            newton_with_dp(points, x)
    dp_time = time.perf_counter() - start
    
    print(f"  Brute force: {brute_time:.6f}s ({brute_time/iterations:.6f}s per run)")
    print(f"  With DP: {dp_time:.6f}s ({dp_time/iterations:.6f}s per run)")
    print(f"  Speedup: {brute_time/dp_time:.2f}x")

def benchmark_regression():
    """Benchmark least squares regression"""
    print("\n📊 Least Squares Regression:")
    
    # Test data with some noise to make regression meaningful
    points = [(i, 2*i + 1 + 0.1*(i%3-1)) for i in range(100)]  # Larger dataset
    iterations = 100
    
    print(f"  Test data: {len(points)} points with linear trend + noise")
    print(f"  Iterations: {iterations} runs each")
    print(f"  Scenario: Finding top-3 worst prediction errors")
    
    # Naive approach: sort all errors to get top 3
    start = time.perf_counter()
    for _ in range(iterations):
        slope, intercept = least_squares_basic(points)
        errors = []
        for x, y in points:
            predicted = slope * x + intercept
            error = abs(y - predicted)
            errors.append(error)
        top_3_naive = sorted(errors, reverse=True)[:3]  # O(n log n)
    basic_time = time.perf_counter() - start
    
    # Heap approach: only track top 3 errors
    start = time.perf_counter()
    for _ in range(iterations):
        least_squares_with_heap(points)  # O(n log k) where k=3
    heap_time = time.perf_counter() - start
    
    print(f"  Naive (sort all): {basic_time:.6f}s ({basic_time/iterations:.6f}s per run)")
    print(f"  Heap (top-K): {heap_time:.6f}s ({heap_time/iterations:.6f}s per run)")
    
    if basic_time > heap_time:
        print(f"  Speedup: {basic_time/heap_time:.2f}x (heap wins)")
        print(f"  Complexity: O(n log n) → O(n log k) where k=3")
    else:
        print(f"  Ratio: {heap_time/basic_time:.2f}x (small dataset - heap overhead)")
        print(f"  Heap wins with larger datasets or smaller k")
    
    # Show results and practical benefit
    slope, intercept, errors = least_squares_with_heap(points)
    print(f"  Linear model: y = {slope:.3f}x + {intercept:.3f}")
    print(f"  Worst 3 errors: {[f'{e:.3f}' for e in errors]}")
    print(f"  Practical use: Outlier detection without storing all errors")

if __name__ == "__main__":
    benchmark_interpolation()
    benchmark_regression()