# The user enters a year.
# The program applies leap year rules using conditions.
# It prints whether the year is a leap year or not.

year = int(input("Year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap year")
else:
    print("Not a leap year")