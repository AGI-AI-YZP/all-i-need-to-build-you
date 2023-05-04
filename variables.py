def perform_calculations(a, b):
    calculations = {
        "Addition": a + b,
        "Subtraction": a - b,
        "Multiplication": a * b,
        "Division": a / b if b != 0 else "undefined",
        "Exponentiation": a ** b,
        "Modulo": a % b if b != 0 else "undefined",
    }
    return calculations

def main():
    # Take user input
    a = float(input("Enter the first number (a): "))
    b = float(input("Enter the second number (b): "))

    # Perform calculations
    results = perform_calculations(a, b)

    # Print the results
    print("\nResults:")
    for operation, result in results.items():
        print(f"{operation}: {a} {operation[0]} {b} = {result}")

if __name__ == "__main__":
    main()