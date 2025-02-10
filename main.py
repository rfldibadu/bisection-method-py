import math

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
        return eval(func, {"x": x, **math.__dict__})

    if f(a) * f(b) >= 0:
        raise ValueError("Error! No root or multiple roots in the given interval.")

    error = abs(b - a)

    iteration = 1  # Track iteration count

    print("\nIteration |      a      |      b      |      c      |    f(c)    |    Error   ")
    print("----------------------------------------------------------------------------")

    while error > error_accept:
        c = (b + a) / 2  # Midpoint
        fc = f(c)

        # Print the iteration details
        print(f"{iteration:^9} | {a:^10.6f} | {b:^10.6f} | {c:^10.6f} | {fc:^10.6f} | {error:^10.6f}")

        if fc == 0:
            return a, b, c, error  # Exact root found

        if f(a) * fc < 0:
            b = c  
        else:
            a = c  

        error = abs(b - a)
        iteration += 1  # Increment iteration count

    print("----------------------------------------------------------------------------")

    return a, b, c, error  # Return final interval, midpoint, and error

# # Example Usage:
# root1, err1 = bisection_method("(4*x**3) + 3*x - 3", 0, 1, 0.05)
# print(f"Root: {root1}, Error: {err1}")

# root2, err2 = bisection_method("(3*x**2) - 4", -2, 0, 0.5)
# print(f"Root: {root2}, Error: {err2}")
