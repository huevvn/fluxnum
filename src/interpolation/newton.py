def newton_interpolation(points, x_approx):
    # Extract x and y values from points
    x_vals, y_vals = zip(*points)
    n = len(points)

    """ Divided Differences """
    def divided_diff(x_vals, y_vals):
        coef = list(y_vals)  # Start with y-values
        for i in range(1, n):
            for j in range(n - 1, i - 1, -1):  # Compute divided differences
                coef[j] = (coef[j] - coef[j - 1]) / (x_vals[j] - x_vals[j - i])
        return coef

    coef = divided_diff(x_vals, y_vals)  # Get coefficients

    """ Evaluate P(x) """
    result = coef[0]  # P0 always exists
    term = 1

    for i in range(1, n):
        term *= (x_approx - x_vals[i - 1])  # Compute (x - x0), (x - x0)(x - x1), etc.
        result += coef[i] * term  # Add next term to the result

    return result