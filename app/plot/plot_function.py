import matplotlib.pyplot as plt
import numpy as np
import math

def plot_function(func, a_values, b_values, midpoints):
    """Plots a function and highlights method steps dynamically."""

    # Define x range dynamically
    x_min, x_max = min(a_values + b_values) - 1, max(a_values + b_values) + 1
    x = np.linspace(x_min, x_max, 400)

    # Compute y-values safely
    y = []
    for val in x:
        try:
            y.append(eval(func, {"x": val, "sin": math.sin, "cos": math.cos, "tan": math.tan,
                                 "log": math.log, "exp": math.exp, "pi": math.pi, "e": math.e}))
        except ValueError:
            y.append(float('nan'))  # Handle invalid function values

    # Set dynamic y-limits
    y_min, y_max = min(y), max(y)
    y_margin = (y_max - y_min) * 0.1  # Add 10% margin
    y_min, y_max = y_min - y_margin, y_max + y_margin

    # Plot function
    plt.figure(figsize=(8, 5))
    plt.plot(x, y, label=f"f(x) = {func}", color='blue')
    plt.axhline(0, color='black', linewidth=1)
    plt.axvline(0, color='black', linewidth=1)

    # Plot points
    plt.scatter(a_values, [0]*len(a_values), color='red', label="Lower bound (a)")
    plt.scatter(b_values, [0]*len(b_values), color='green', label="Upper bound (b)")
    plt.scatter(midpoints, [0]*len(midpoints), color='purple', marker='x', label="Midpoints (c)")

    # Dynamic axis limits
    plt.xlim(x_min, x_max)
    plt.ylim(y_min, y_max)

    # Auto-tick placement
    plt.xticks(np.linspace(x_min, x_max, 7))  # 7 evenly spaced ticks
    plt.yticks(np.linspace(y_min, y_max, 7))

    # Labels & display
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title("Bisection & False Position Method Iterations")
    plt.legend()
    plt.grid()
    plt.show()
