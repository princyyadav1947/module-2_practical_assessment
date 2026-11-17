# College canteen card system

balance = 500
correct_pin = 4321
attempt = 0

# PIN Validation
while attempt < 3:
    pin = int(input("Enter PIN: "))

    if pin == correct_pin:
        print("Login Successful")
        break
    else:
        print("Wrong PIN")
        attempt += 1
        continue

if attempt == 3:
    print("Card Blocked")


# Conditional Statements
else:
    while True:
        print("\n1. Check Balance")
        print("2. Recharge")
        print("3. Make Purchase")
        print("4. View History")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            print("Balance:", balance)

        elif choice == "2":
            amount = int(input("Enter recharge amount: "))

            if amount <= 0:
                print("Invalid amount")
            else:
                balance += amount
                print("Recharge Successful")

        elif choice == "3":
            amount = int(input("Enter purchase amount: "))

            if amount <= 0:
                print("Invalid amount")
            elif amount > balance:
                print("Insufficient Balance")
            else:
                balance = amount
                print("Purchase Successful")

        elif choice == "4":
            pass

        elif choice == "5":
            print("Final Balance:", balance)
            break

        else:
            print("Invalid Choice")

    