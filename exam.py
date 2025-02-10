from main import bisection_method
# import argparse

# def main():
#     parser = argparse.ArgumentParser(description="Find the root of a function using the Bisection Method.")

#     parser.add_argument("function", type=str, help="The function in terms of x (e.g., '4*x**3 + 3*x - 3')")
#     parser.add_argument("a", type=float, help="Lower boundary (a)")
#     parser.add_argument("b", type=float, help="Upper boundary (b)")
#     parser.add_argument("error_accept", type=float, help="Acceptable error threshold")

#     args = parser.parse_args()

#     try:
#         root, error = bisection_method(args.function, args.a, args.b, args.error_accept)
#         print(f"Root: {root}, Final Error: {error}")
#     except ValueError as e:
#         print(f"Error: {e}")

# if __name__ == "__main__":
#     main()


def main():
    print("=== Bisection Method Solver ===")

    func = input("Enter the function in terms of x (e.g., '4*x**3 + 3*x - 3'): ")
    
    while True:
        try:
            a = float(input("Enter the lower boundary (a): "))
            b = float(input("Enter the upper boundary (b): "))
            if a >= b:
                print("Error: Lower boundary (a) must be less than upper boundary (b). Try again.")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter a number.")

    while True:
        try:
            error_accept = float(input("Enter the acceptable error threshold: "))
            if error_accept <= 0:
                print("Error: Error threshold must be greater than zero. Try again.")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter a number.")

    try:
        lower_bound, upper_bound, midpoint, error = bisection_method(func, a, b, error_accept)
        print(f"\nThe root is between: {lower_bound} and {upper_bound}")
        print(f"Estimated root (midpoint): {midpoint}")
        print(f"Final Error: {error}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()