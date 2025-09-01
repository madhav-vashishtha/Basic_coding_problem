password = input("Enter your password: ")
length = len(password)

if length <6:
    print("Weak Password")
elif length >6 and length <10:
    print("Medium Strength Password")
else:
    print("Strong Password")