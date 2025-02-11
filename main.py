import math
import matplotlib.pyplot as plt
import numpy as np

def bisection_method(func, a, b, error_accept):
    """
    Parameters:
    --------------------------------
    :param func: The user-defined function as a string (in terms of 'x').
    :param a: The initial lower root boundary. 
    :param b: The initial upper root boundary.
    :param error_accept: The user's acceptable level of error.

    Returns:
    --------------------------------
    :return: The approximate root and the error at the final iteration.
    """
    def f(x):
        return eval(func, {"x": x, "sin": math.sin, "cos": math.cos, "tan": math.tan,
                           "log": math.log, "exp": math.exp, "pi": math.pi, "e": math.e})

    if f(a) * f(b) >= 0:
        raise ValueError("Error! No root or multiple roots in the given interval.")

    error = abs(b - a)
    iteration = 1

    # Store iterations for plotting
    midpoints = []
    a_values = [a]
    b_values = [b]

    print("\nIteration |      a      |      b      |      c      |    f(c)    |    Error   ")
    print("----------------------------------------------------------------------------")

    while error > error_accept:
        c = (b + a) / 2  # Midpoint
        fc = f(c)

        # Store midpoint
        midpoints.append(c)
        a_values.append(a)
        b_values.append(b)

        # Print iteration details
        print(f"{iteration:^9} | {a:^10.6f} | {b:^10.6f} | {c:^10.6f} | {fc:^10.6f} | {error:^10.6f}")

        if fc == 0:
            break  # Exact root found

        if f(a) * fc < 0:
            b = c  
        else:
            a = c  

        error = abs(b - a)
        iteration += 1

    print("----------------------------------------------------------------------------")

    # Plot function and iterations
    print(f"Final Interval: a = {a}, b = {b}")
    print(f"Approximate Root: {c}, Final Error: {error}")

    # Plot function and iterations as the last output
    plot_function(func, a_values, b_values, midpoints)

    return a, b, c, error  # Return final interval, midpoint, and error

def plot_function(func, a_values, b_values, midpoints):
    """Plots a function and highlights bisection method steps dynamically."""
    
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
    plt.title("Bisection Method Iterations")
    plt.legend()
    plt.grid()
    plt.show()
