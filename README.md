# FluxNum ⚡️

FluxNum is a numerical analysis tool for interpolation, supporting Newton and Lagrange methods.

## ✨ Features

-   Newton Interpolation
-   Lagrange Interpolation
-   Quadratic Interpolation Support
-   Command-line interface (CLI) for easy interaction

## 🔧 Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/fluxnum.git
    cd fluxnum
    ```

2. Create a virtual environment and activate it:

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## ⚙️ Running & Interacting

Run the application:

```sh
python src/run.py
```

```sh
╭───────────────────────╮
│ Welcome to FluxNum ⚡️ │
╰───────────────────────╯
❯ Choose a Method: Interpolation
❯ Choose an interpolation method: Newton

💡 Using Newton method ℕ

❯ Choose the Interpolation degree: Linear
🎯 Linear Interpolation

📌 Enter Point 1
❯ Enter x1: 0
❯ Enter f(0.0): 1
📌 Enter Point 2
❯ Enter x2: 2
❯ Enter f(2.0): 3

≈ Approximation Input
❯ Enter the x value to approximate: 0.765

🚀 Computing Interpolation...
⏳ Processing... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:02

╭──────────────── FluxNum Results ─────────────────╮
│                                                  │
│ 📊 Calculation Summary                           │
│ ✔ Method: Newton Interpolation                   │
│ ✔ Degree: 1                                      │
│ ✔ Points: [(0.0, 1.0), (2.0, 3.0)]               │
│ ✔ Approximation: f(0.765) =  1.7650000000000001  │
│                                                  │
╰──────────────────────────────────────────────────╯
```

## 📚 Documentation

-   📄 [Newton Interpolation](docs/newton_interpolation.md)
-   📄 [Lagrange Interpolation](docs/lagrange_interpolation.md)
-   📄 [Interpolation Comparison](docs/interpolation_comparison.md)
