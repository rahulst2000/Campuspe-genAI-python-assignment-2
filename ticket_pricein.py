# This simple program works directly with the person running it.
# It repeatedly asks them to type in an age and then tells them how much
#a ticket costs based on that age.  After showing the price it asks
# whether they want to calculate again.  Typing "yes" or "y" repeats
# the process any other answer stops the program.

while True:
    age = int(input("Enter age: "))

    if age <= 5:
        price = 0
    elif age <= 12:
        price = 10
    else:
        price = 20

    print("Ticket price:", price)

    continue_calculation = input("Do you want to calculate ticket price for another age (yes/no): ")
    if continue_calculation.lower() not in ("yes", "y"):
        break