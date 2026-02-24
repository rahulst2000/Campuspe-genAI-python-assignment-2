#This program converts temperature between Celsius and Fahrenheit.
#User selects the conversion type from a menu.
#the program runs continuously to allow multiple calculations.
#It stops only when the user chooses to exit.
while True:
    print("\nTemperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")

    choice = input("Enter choice (1 or 2): ")

    if choice == "1":
        c = float(input("Enter temperature in Celsius: "))
        f = c * 9/5 + 32
        print("Fahrenheit:", f)

    elif choice == "2":
        f = float(input("Enter temperature in Fahrenheit: "))
        c = (f - 32) * 5/9
        print("Celsius:", c)

    else:
        print("Invalid choice. Try again.")

    again = input("Do you want another conversion? (yes/no): ").lower()
    if again != "yes":
        print("Program ended.")
        break