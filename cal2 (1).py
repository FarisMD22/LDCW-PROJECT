def add(x: float, y: float) -> float:
    """Returns the sum of x and y."""
    return x + y

def subtract(x: float, y: float) -> float:
    """Returns the difference between x and y."""
    return x - y

def multiply(x: float, y: float) -> float:
    """Returns the product of x and y."""
    return x * y

def divide(x: float, y: float) -> float:
    """Returns the quotient of x and y. If y is 0, raises a ValueError."""
    if y == 0:
        raise ValueError("Error! Division by zero.")
    return x / y

def get_number(prompt: str) -> float:
    """Prompts the user to enter a number and returns it."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def calculator() -> None:
    """Main function to perform calculator operations."""
    operations = {
        '1': ("Add", add),
        '2': ("Subtract", subtract),
        '3': ("Multiply", multiply),
        '4': ("Divide", divide)
    }

    print("Select operation:")
    for key, (name, _) in operations.items():
        print(f"{key}. {name}")

    while True:
        choice = input("Enter choice (1/2/3/4): ")

        if choice in operations:
            num1 = get_number("Enter first number: ")
            num2 = get_number("Enter second number: ")

            operation_name, operation_func = operations[choice]
            try:
                result = operation_func(num1, num2)
                print(f"The result of {operation_name.lower()} is: {result}")
            except ValueError as e:
                print(e)

            next_calculation = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
            if next_calculation != 'yes':
                break
        else:
            print("Invalid choice. Please select a valid operation.")

if __name__ == "__main__":
    calculator()
