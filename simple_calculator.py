while True:
    Num_one = float(input("Enter the first number : "))
    operator = input("Enter_operator +,-,*, / : ")
    Num_two = float(input("Enter the second number : "))
    if operator == "+":
        sum = Num_one + Num_two
        print("Sum: ", sum)
    elif operator == "-":
        Diffrence = Num_one - Num_two
        print("Difference: ", Diffrence)
    elif operator == "*":
        Multiplication = Num_one * Num_two
        print("Multiplication: ", Multiplication)
    elif operator == "/":
        if Num_two != 0:
            Division = Num_one / Num_two
            print("Division: ", Division)
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Invalid operator. Please enter +, -, *, or /.")
    cal_continue = input("Do you want to continue with more calculation? (yes/no) : ")
    if cal_continue.lower() not in ("yes", "y"):
        print("thank you")
        break