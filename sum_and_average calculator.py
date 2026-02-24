# Sum and Average Calculator (Easy Level)
# This program takes numbers from the user separated by spaces.
# It finds and prints the total sum and average of those numbers.

numbers = input("Enter numbers separated by space: ")
parts = numbers.split()

total = 0
count = 0

for x in parts:
    total = total + float(x)
    count = count + 1

print("Sum:", total)
print("Average:", total / count)