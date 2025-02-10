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
    plot_function(func, a_values[0], b_values[0], midpoints, a_values, b_values)

    return a, b, c, error  # Return final interval, midpoint, and error


def plot_function(func, a_start, b_start, midpoints, a_values, b_values):
    """ Plots the function and the bisection method iterations. """
    # Check if log(x) is in the function string
    if "log(" in func:
        x = np.linspace(0.01, 6, 400)  # Avoid log(0) and negative values
    else:
        x = np.linspace(-2, 2, 400)  # Allow negative values for other functions

    # Safely evaluate the function
    y = []
    for val in x:
        try:
            y.append(eval(func, {"x": val, "sin": math.sin, "cos": math.cos, "tan": math.tan,
                                 "log": math.log, "exp": math.exp, "pi": math.pi, "e": math.e}))
        except ValueError:
            y.append(float('nan'))  # Handle domain errors (e.g., log(negative number))

    plt.figure(figsize=(8, 5))
    plt.plot(x, y, label=f"f(x) = {func}", color='blue')  # Function curve
    plt.axhline(0, color='black', linewidth=1)  # x-axis
    plt.axvline(0, color='black', linewidth=1)  # y-axis

    # Plot a, b boundaries
    plt.scatter(a_values, [0]*len(a_values), color='red', label="Lower bound (a)")
    plt.scatter(b_values, [0]*len(b_values), color='green', label="Upper bound (b)")

    # Plot midpoints
    plt.scatter(midpoints, [0]*len(midpoints), color='purple', marker='x', label="Midpoints (c)")

    # Set axis limits
    plt.xlim(-2, 2)  # X-axis from -2 to 2
    plt.ylim(-6, 6)  # Y-axis from -6 to 6

    # Adjust tick intervals
    plt.xticks(np.arange(-2, 3, 1))  # X-axis ticks every 1 unit
    plt.yticks(np.arange(-6, 7, 2))  # Y-axis ticks every 2 units

    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title("Bisection Method Iterations")
    plt.legend()
    plt.grid()
    plt.show()
