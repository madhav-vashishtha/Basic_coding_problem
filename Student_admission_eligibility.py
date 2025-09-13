maths = int(input("enter maths marks: "))
physics = int(input("enter physics marks: "))
chemistry =int(input("enter chemistry marks: "))

if (maths >= 65 and physics >= 55 and chemistry >= 50) and\
    ((maths + physics + chemistry >= 180) or (maths + physics >= 140)):
    print("Student is Eligible for Admission ")
else:
    print("Student is NOT Eligible for Admission")