import questionary
from rich.console import Console
from rich.progress import track
import time

console = Console()

console.print("\n[bold cyan]Welcome to FluxNum ⚡️[/bold cyan]\n")

topic = questionary.select(
    "Choose a Method:",
    qmark="❯",
    choices=["Least Squares", "Interpolation"],
).ask()

if topic == "Interpolation":
    method = questionary.select(
        "Choose an interpolation method:",
        qmark="❯",
        choices=["Lagrange", "Newton"],
    ).ask()

    # Display method symbol
    method_symbol = "ℒ" if method == "Lagrange" else "ℕ"
    console.print(f"💡 [yellow]{topic} using {method} method {method_symbol}[/yellow]\n")

    # Degree Selection with Numeric Mapping
    degree_map = {"Linear": 1, "Quadratic": 2, "Bicubic": 3}
    degree_str = questionary.select(
        "Choose the Interpolation degree:",
        qmark="❯",
        choices=list(degree_map.keys()),
    ).ask()
    degree = degree_map[degree_str]  # Convert string to integer

    console.print(f"🎯 [green]{degree_str} Interpolation[/green]\n")

    # Collecting Points
    points = []
    for i in range(0, degree + 1):  # Degree + 1 points required
        console.print(f"[bold cyan]📌 Point {i}[/bold cyan]")  # Fixed MarkupError
        x = float(questionary.text(qmark="❯", message=f"Enter x{i}:").ask())
        y = float(questionary.text(qmark="❯", message=f"Enter f({x}):").ask())
        points.append((x, y))

    console.print("\n[bold red]≈ Approximation[/bold red]")  # Fixed MarkupError
    x_approx = float(questionary.text(qmark="❯", message="Enter the x value to approximate:").ask())

    # Animated "Solving" Effect
    console.print("\n[yellow]🚀 Computing Interpolation...[/yellow]")
    for _ in track(range(25), description="⏳ Processing..."):
        time.sleep(0.3)

    # Display Results
    console.print("\n[bold red]📊 Calculation Summary[/bold red]")
    console.print(f"✔ Method: [magenta]{method} {topic} method[/magenta]")
    console.print(f"✔ Degree: [green]{degree_str}[/green]")
    console.print(f"✔ Points: [white]{points}[/white]")
    console.print(f"✔ Approximation: f([bold red]{x_approx}[/bold red]) = [black yellow]{x_approx}[/black yellow]\n")

else:
    console.print("[blue]🌀 Sorry, Least Squares is under development[/blue]")
