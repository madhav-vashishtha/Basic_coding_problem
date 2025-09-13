age=int(input("enter the age: "))
fare=float(input("enter ticket fare: "))
gender=input("enter gender(male/female): ")
finalfare=0
if age<5:
   finalfare=0
elif age>=60:
    finalfare=fare*0.5
elif gender=="female"and age>=18 or age<=59:
    finalfare=fare*0.25
else:
    finalfare=fare

print("final ticket fare",finalfare)