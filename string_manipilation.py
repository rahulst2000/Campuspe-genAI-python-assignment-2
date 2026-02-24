# Simple String Manipulator
while True:
    user_input = input("Enter a string: ")

    # Reverse the string
    reversed_string = user_input[::-1]
    print("Reversed string:", reversed_string)

    # Convert to uppercase
    upper_case = user_input.upper()
    print("Uppercase:", upper_case)

    # Convert to lowercase
    lower_case = user_input.lower()
    print("Lowercase:", lower_case)

    # Check if a substring exists
    substring = input("Enter a substring to search for: ")
    if substring in user_input:
        print(f"Yes, '{substring}' is in the string.")
    else:
        print(f"No, '{substring}' is not in the string.")

    another_manipulation = input("Do you want to manipulate another string? (yes/no,y/n): ")
    if another_manipulation.lower() not in ("yes", "y"):
        print("Thank you for using the string manipulator!")
        break
