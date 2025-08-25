age= int(input("enter the age:"))
if age<13:
    print("CHILD")
elif age>=13 and age<=19:
    print("TEENAGE")
elif age>=20 and age<=59:
    print("ADULT")
else:
    print("SENIOR")
    