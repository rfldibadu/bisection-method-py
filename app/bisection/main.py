import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from app.plot import plot_function
import math

def bisection_method(func, a, b, error_accept):
    def f(x):
        return eval(func, {"x": x, "sin": math.sin, "cos": math.cos, "tan": math.tan,
                           "log": math.log, "exp": math.exp, "pi": math.pi, "e": math.e})

    if f(a) * f(b) >= 0:
        raise ValueError("Error! No root or multiple roots in the given interval.")

    error = float("inf")
    iteration = 1

    midpoints = []
    a_values = [a]
    b_values = [b]

    print("\nIteration |      a      |      b      |      c      |    f(c)    |    Error   ")
    print("----------------------------------------------------------------------------")

    while error > error_accept:
        c = (a + b) / 2
        fc = f(c)

        midpoints.append(c)
        a_values.append(a)
        b_values.append(b)

        print(f"{iteration:^9} | {a:^10.6f} | {b:^10.6f} | {c:^10.6f} | {fc:^10.6f} | {error:^10.6f}")

        if abs(fc) < error_accept:
            break

        if f(a) * fc < 0:
            b = c
        else:
            a = c

        error = abs(b - a)
        iteration += 1

    print("----------------------------------------------------------------------------")
    print(f"Final Interval: a = {a}, b = {b}")
    print(f"Approximate Root: {c}, Final Error: {error}")

    plot_function(func, a_values, b_values, midpoints)  # Call plot function

    return a, b, c, error
