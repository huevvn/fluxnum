import time
import questionary
from rich.console import Console
from rich.panel import Panel

from interpolation.lagrange import lagrange_interpolation, lagrange_with_hashing
from interpolation.newton import newton_interpolation, newton_with_dp
from interpolation.regression import least_squares_basic, least_squares_with_heap, predict_linear

console = Console()

def display_welcome():
    console.print(Panel.fit("[bold cyan]FluxNum - Simple DSA Edition[/bold cyan]"))

def get_method_choice():
    return questionary.select(
        "Choose method:",
        choices=["Interpolation", "Least Squares Regression"],
    ).ask()

def get_interpolation_method():
    return questionary.select(
        "Choose interpolation method:",
        choices=["Lagrange", "Newton"],
    ).ask()

def get_optimization_choice():
    return questionary.select(
        "Choose version:",
        choices=["Basic (Brute Force)", "DSA Optimized", "Compare Both"],
    ).ask()

def collect_points():
    points = []
    n = int(questionary.text("How many points?").ask())
    
    for i in range(n):
        console.print(f"[cyan]Point {i + 1}[/cyan]")
        x = float(questionary.text(f"x{i + 1}:").ask())
        y = float(questionary.text(f"y{i + 1}:").ask())
        points.append((x, y))
    
    return points

def get_approximation_x():
    return float(questionary.text("Enter x value to interpolate:").ask())

def run_interpolation():
    method = get_interpolation_method()
    optimization = get_optimization_choice()
    points = collect_points()
    x_approx = get_approximation_x()
    
    console.print(f"\n[yellow]Computing with {len(points)} points...[/yellow]")
    
    if optimization == "Compare Both":
        # Time both versions
        if method == "Lagrange":
            start = time.perf_counter()
            result1 = lagrange_interpolation(points, x_approx)
            time1 = time.perf_counter() - start
            
            start = time.perf_counter()
            result2 = lagrange_with_hashing(points, x_approx)
            time2 = time.perf_counter() - start
            
            console.print(f"\n[green]Results:[/green]")
            console.print(f"Basic: {result1:.8f} ({time1:.6f}s)")
            console.print(f"DSA:   {result2:.8f} ({time2:.6f}s)")
            console.print(f"Speedup: {time1/time2:.2f}x")
        
        else:  # Newton
            start = time.perf_counter()
            result1 = newton_interpolation(points, x_approx)
            time1 = time.perf_counter() - start
            
            start = time.perf_counter()
            result2 = newton_with_dp(points, x_approx)
            time2 = time.perf_counter() - start
            
            console.print(f"\n[green]Results:[/green]")
            console.print(f"Basic: {result1:.8f} ({time1:.6f}s)")
            console.print(f"DSA:   {result2:.8f} ({time2:.6f}s)")
            console.print(f"Speedup: {time1/time2:.2f}x")
    
    else:
        # Single version
        use_dsa = optimization == "DSA Optimized"
        
        start = time.perf_counter()
        if method == "Lagrange":
            result = lagrange_with_hashing(points, x_approx) if use_dsa else lagrange_interpolation(points, x_approx)
        else:
            result = newton_with_dp(points, x_approx) if use_dsa else newton_interpolation(points, x_approx)
        exec_time = time.perf_counter() - start
        
        version = "DSA" if use_dsa else "Basic"
        console.print(f"\n[green]{method} ({version}): {result:.8f}[/green]")
        console.print(f"[cyan]Time: {exec_time:.6f}s[/cyan]")

def run_regression():
    optimization = get_optimization_choice()
    points = collect_points()
    
    console.print(f"\n[yellow]Computing regression with {len(points)} points...[/yellow]")
    
    if optimization == "Compare Both":
        start = time.perf_counter()
        slope, intercept = least_squares_basic(points)
        time1 = time.perf_counter() - start
        
        start = time.perf_counter()
        slope2, intercept2, errors = least_squares_with_heap(points)
        time2 = time.perf_counter() - start
        
        console.print(f"\n[green]Results:[/green]")
        console.print(f"Basic: y = {slope:.4f}x + {intercept:.4f} ({time1:.6f}s)")
        console.print(f"DSA:   y = {slope2:.4f}x + {intercept2:.4f} ({time2:.6f}s)")
        console.print(f"Top errors: {[f'{e:.3f}' for e in errors[:3]]}")
    
    else:
        use_dsa = optimization == "DSA Optimized"
        
        start = time.perf_counter()
        if use_dsa:
            slope, intercept, errors = least_squares_with_heap(points)
            console.print(f"\n[green]Linear model: y = {slope:.4f}x + {intercept:.4f}[/green]")
            console.print(f"[yellow]Top 3 errors: {[f'{e:.3f}' for e in errors[:3]]}[/yellow]")
        else:
            slope, intercept = least_squares_basic(points)
            console.print(f"\n[green]Linear model: y = {slope:.4f}x + {intercept:.4f}[/green]")
        
        exec_time = time.perf_counter() - start
        console.print(f"[cyan]Time: {exec_time:.6f}s[/cyan]")
    
    # Test prediction
    if questionary.confirm("Test prediction?").ask():
        x_test = float(questionary.text("Enter x value:").ask())
        prediction = predict_linear(x_test, slope, intercept)
        console.print(f"[magenta]Prediction: f({x_test}) = {prediction:.4f}[/magenta]")

def main():
    display_welcome()
    method = get_method_choice()
    
    if method == "Interpolation":
        run_interpolation()
    else:
        run_regression()

if __name__ == "__main__":
    main()
