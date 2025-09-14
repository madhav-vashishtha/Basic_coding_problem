''' Quadratic Equation Roots
Input coefficients (a, b, c) and 
print if roots are real, equal, or imaginary.'''

a=float(input("enter coefficient a: "))
b=float(input("enter coefficient b: "))
c=float(input("enter coefficient c: "))

D =b**2 - 4*a*c

if D > 0:
    print("Roots are real and unequal.")
elif D == 0:
    print("Roots are real and equal.")
else:
    print("Roots are imaginary.")
