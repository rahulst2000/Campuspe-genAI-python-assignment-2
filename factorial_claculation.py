# The user enters a number.
# The program multiplies all numbers from 1 up to that number.
# The final result is printed as the factorial.

n = int(input("Number: "))
fact = 1
for i in range(1, n+1):
    fact *= i
print("Factorial:", fact)