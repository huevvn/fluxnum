import time
import questionary
from rich.console import Console
from rich.progress import track
from rich.panel import Panel

# Initialize Console
console = Console()

def display_welcome():
    """ The Welcome Message """
    console.print(Panel.fit("[bold cyan]Welcome to FluxNum ⚡️[/bold cyan]"))

def get_user_selection():
    """ Interpolation or Least Squares """
    return questionary.select(
        "Choose a Method:",
        qmark="❯",
        choices=["Least Squares", "Interpolation"],
    ).ask()

def get_interpolation_method():
    """ Lagrange / Newton """
    method = questionary.select(
        "Choose an interpolation method:",
        qmark="❯",
        choices=["Lagrange", "Newton"],
    ).ask()
    
    method_symbol = "ℒ" if method == "Lagrange" else "ℕ"
    console.print(f"\n💡 [yellow]Using {method} method {method_symbol}[/yellow]\n")
    return method

def get_interpolation_degree():
    """ Degree of interpolation """
    degree_map = {"Linear": 1, "Quadratic": 2, "Bicubic": 3}
    degree_str = questionary.select(
        "Choose the Interpolation degree:",
        qmark="❯",
        choices=list(degree_map.keys()),
    ).ask()
    
    console.print(f"🎯 [green]{degree_str} Interpolation[/green]\n")
    return degree_map[degree_str]

def collect_points(degree):
    """ Collect user input for points """
    points = []
    for i in range(degree + 1):
        console.print(f"[bold cyan]📌 Enter Point {i + 1}[/bold cyan]")
        x = float(questionary.text(qmark="❯", message=f"Enter x{i + 1}:").ask())
        y = float(questionary.text(qmark="❯", message=f"Enter f({x}):").ask())
        points.append((x, y))
    return points

def get_approximation_x():
    """ Ask the user for the x value to approximate """
    console.print("\n[bold red]≈ Approximation Input[/bold red]")
    return float(questionary.text(qmark="❯", message="Enter the x value to approximate:").ask())

def show_processing_animation():
    """ Show the animated progress bar """
    console.print("\n[yellow]🚀 Computing Interpolation...[/yellow]")
    for _ in track(range(25), description="⏳ Processing...\n"):
        time.sleep(0.1)

def display_results(method, degree, points, x_approx):
    """ Final Results """
    console.print(Panel.fit(f"""
📊 [bold red]Calculation Summary[/bold red]
✔ Method: [magenta]{method} Interpolation[/magenta]
✔ Degree: [green]{degree}[/green]
✔ Points: [white]{points}[/white]
✔ Approximation: f([bold red]{x_approx}[/bold red]) = [black on cyan] f(x) [/black on cyan]
""", title="FluxNum Results"))

# Main Program Flow
display_welcome()
topic = get_user_selection()

if topic == "Interpolation":
    method = get_interpolation_method()
    degree = get_interpolation_degree()
    points = collect_points(degree)
    x_approx = get_approximation_x()
    show_processing_animation()
    display_results(method, degree, points, x_approx)
else:
    console.print("[red]🌀 Sorry, Least Squares is under development[/red]")
