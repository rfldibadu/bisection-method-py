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
        return eval(func, {"x": x, **math.__dict__})  # Allows sin, cos, etc.

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
    x = np.linspace(a_start - 1, b_start + 1, 400)  # Range for function plotting
    y = [eval(func, {"x": val, **math.__dict__}) for val in x]

    plt.figure(figsize=(8, 5))
    plt.plot(x, y, label=f"f(x) = {func}", color='blue')  # Function curve
    plt.axhline(0, color='black', linewidth=1)  # x-axis
    plt.axvline(0, color='black', linewidth=1)  # y-axis

    # Plot a, b boundaries
    plt.scatter(a_values, [0]*len(a_values), color='red', label="Lower bound (a)")
    plt.scatter(b_values, [0]*len(b_values), color='green', label="Upper bound (b)")

    # Plot midpoints
    plt.scatter(midpoints, [0]*len(midpoints), color='purple', marker='x', label="Midpoints (c)")

    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title("Bisection Method Iterations")
    plt.legend()
    plt.grid()
    plt.show()


# # Example Usage:
# root1, err1 = bisection_method("(4*x**3) + 3*x - 3", 0, 1, 0.05)
# print(f"Root: {root1}, Error: {err1}")

# root2, err2 = bisection_method("(3*x**2) - 4", -2, 0, 0.5)
# print(f"Root: {root2}, Error: {err2}")
