'''Triangle Type
If valid triangle, print Equilateral, Isosceles, or Scalene.'''

a=int(input("enter side a: "))
b=int(input("enter side b: "))
c=int(input("enter side c: "))

if (a + b > c) and (a + c > b) and (b + c > a):
    if a == b == c:
        print("Equilateral")
    elif a == b or b == c or a == c:
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("Not a Valid Triangle")