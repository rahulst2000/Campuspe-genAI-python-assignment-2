# This program converts a decimal number into binary, octal, and hexadecimal.
# The user enters a number.
# The program displays the number in different number systems.

num = int(input("Enter number: "))
print("Binary:", bin(num)[2:])
print("Octal:", oct(num)[2:])
print("Hexadecimal:", hex(num)[2:])