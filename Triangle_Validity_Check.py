a= float(input("enter the side a:"))
b= float(input("enter the side b:"))
c= float(input("enter the side c:"))
if (a+b)>c and (b+c)>a and (a+c)>b:
    print("VALID TRIANGLE")
else:
    print("NOT VALID")
    