# Clearance level projects in python
print("Lets determine your clearance: \n")
name =input("Enter your name: \n")
clearance_level = input("Enter your clearance level: \n 1 - Secret\n 2- Confidential \n 3-Others\n")
if clearance_level == "1":
    print("Welcome you are our secret agent")
elif clearance_level == "2":
    print("Welcome you are our confidential agent")
else:
    print("Access denied")
