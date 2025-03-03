def lagrange_interpolation(points, x_approx):

    n = len(points)
    px = 0

    for i in range(n):
        xi, yi = points[i]
        fxi = yi
        for j in range(n):
            if i != j:
                xj = points[j][0]
                fxi *= (x_approx - xj) / (xi - xj)
        px += fxi

    return float(px)  # This is f(x_approx)
