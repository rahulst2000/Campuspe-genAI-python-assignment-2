# simple ATM system.
# The user can check balance, deposit money, or withdraw money.
# The balance updates after each transaction.
# The program runs repeatedly until the user chooses to exit.

balance = 1000
while True:
    print("1. Check Balance\n2. Deposit\n3. Withdraw\n4. Exit")
    choice = input("Choose: ")
    if choice == "1":
        print("Balance:", balance)
    elif choice == "2":
        amt = float(input("Deposit amount: "))
        balance += amt
    elif choice == "3":
        amt = float(input("Withdraw amount: "))
        if amt <= balance:
            balance -= amt
        else:
            print("Insufficient funds.")
    elif choice == "4":
        break
    else:
        print("Invalid choice.")