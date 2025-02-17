from main import false_position_method

def main():
    print("=== False Position (Regula Falsi) Method Solver ===")

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
        lower_bound, upper_bound, root, error = false_position_method(func, a, b, error_accept)
        print(f"\nThe root is between: {lower_bound} and {upper_bound}")
        print(f"Estimated root: {root}")
        print(f"Final Error: {error}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()