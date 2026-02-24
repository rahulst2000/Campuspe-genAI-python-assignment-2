# Bill Splitter (Easy Level)
# This program calculates how much each person should pay from a total bill.
# The user enters the total bill amount and number of people.
# If the number of people is greater than zero, the bill is divided equally.
# If the number of people is zero or negative, it shows an error message.
while True:
    total = float(input("Total bill: "))
    people = int(input("Number of people: "))
    if people > 0:
        print("Each pays:", total / people)
    else:
        print("Invalid number of people.")

    another_bill = input("Do you want to calculate another bill? (yes/no,y/n): ")
    if another_bill.lower() not in ("yes", "y"):
        print("Thank you for using the bill splitter!")
        break
