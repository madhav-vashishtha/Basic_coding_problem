m1=int(input("enter marks of subject 1: "))
m2=int(input("enter marks of subject 2: "))
m3=int(input("enter marks of subject 3: "))
average= (m1+m2+m3) /3

if m1>=40 and m2>=40 and m3>=40 and average>=50:
    print("result: PASS")
else:
    print("result: FAIL")