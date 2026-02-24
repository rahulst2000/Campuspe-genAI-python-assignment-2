while True:
    age = int(input("Enter age: "))
    if age <= 5:
        price = 0
    elif (age >5) and (age <=12) :
        price = 10
    else:
        price = 20
    print("Ticket price:", price)
    continue_calculation = input("Do you want to calculate ticket price for another age (yes/no): ")
    if continue_calculation.lower() not in ("yes", "y"):
        break