def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero is not allowed"

print("Welcome to Felix's calculator!")

while True:
    print("Choose what you want to calculate:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Quit")

    choice = input("Enter the number of the desired operation: ")

    if choice == "5":
        print("Calculator is closing. Goodbye!")
        break

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if choice == "1":
        result = add(num1, num2)
        print("Result: ", result)
    elif choice == "2":
        result = subtract(num1, num2)
        print("Result: ", result)
    elif choice == "3":
        result = multiply(num1, num2)
        print("Result: ", result)
    elif choice == "4":
        result = divide(num1, num2)
        print("Result: ", result)
    else:
        print("Invalid choice. Please enter a valid number.")
