# The user enters a number.
# The program multiplies the number from 1 to 10.
# Each result is displayed as a multiplication table.

num = int(input("Number: "))
for i in range(1, 11):
    print(num, "x", i, "=", num * i)