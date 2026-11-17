# Simple ATM Simulation

# balance = 10000
# pin = 1234
# attempt = 0
# login = False

# PIN verification
# while attempt < 3:

#     user_pin = int(input("Enter PIN: "))

#     if user_pin == pin:
#         print("Login successful")
#         login = True
#         break

#     else:
#         attempt += 1
#         print("Wrong PIN")

# if login == False:
#     print("Account locked")

# ATM Menu
# if login == True:

#     while True:

#         print("\n1. Check Balance")
#         print("2. Deposit")
#         print("3. Withdraw")
#         print("4. Change PIN")
#         print("5. Exit")

#         choice = input("Enter choice: ")

#         if choice == "1":
#             print("Balance:", balance)

#         elif choice == "2":
#             amount = float(input("Enter amount: "))

#             if amount < 0:
#                 print("Invalid amount")
#                 continue

        #     balance += amount
        #     print("New Balance:", balance)

        # elif choice == "3":
        #     amount = float(input("Enter amount: "))

        #     if amount < 0:
        #         print("Invalid amount")

        #     elif amount > balance:
        #         print("Insufficient balance")

        #     else:
        #         balance -= amount
        #         print("New Balance:", balance)

        # elif choice == "4":
        #     pass

        # elif choice == "5":
        #     print("Final Balance:", balance)
        #     print("Thank you")
        #     break

        # else:
        #     print("Invalid choice")
            