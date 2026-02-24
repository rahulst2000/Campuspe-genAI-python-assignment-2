# This program performs basic arithmetic operations.
# It uses functions for add, subtract, multiply and divide.
# User selects an operation from the menu and enters two numbers.
# If the user enters an option outside the selection range, it asks to enter a correct choice.
# The program repeats until the user decides to stop.

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
        return "Cannot divide by zero"

while True:
    print("\nSimple Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice (1-4): ")

    if choice not in ["1", "2", "3", "4"]:
        print("Enter correct choice from 1 to 4")
        continue

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == "1":
        print("Result:", add(num1, num2))
    elif choice == "2":
        print("Result:", subtract(num1, num2))
    elif choice == "3":
        print("Result:", multiply(num1, num2))
    elif choice == "4":
        print("Result:", divide(num1, num2))

    again = input("Do you want another calculation? (yes/no): ").lower()
    if again != "yes":
        print("Calculator stopped.")
        break