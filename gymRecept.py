# Gym Reception Desk

#Taking member details
name = input("Enter member name:")
age = int(input("Enter age:"))
classes = int(input("Enter  no. of booked classes:"))
fee = float(input("Enter monthly fee:"))
active = input("Active membership (yes/no):")

membership = active == "yes"

classes += 1

check_name = "e" in name
check_age = age > 15
check_classes = classes < 4

eligible = (membership is True) 
check_age and check_classes

#Displsy Details

print("\n-Gym member summary-")
print("name:", name)
print("age:", age)
print("classes:", classes)
print(" monthly fee: rs.", fee)
print("membership active:", membership )
print("Name contains e:", check_name)
print("Eligible:", eligible) 





