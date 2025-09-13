salary=float(input("enter the salary: "))
service=int(input("enter the service: "))

if service >10:
    bonus =0.10*salary
elif service >6 and service <10:
    bonus=0.8*salary
else:
    bonus=0.5*salary
print("your bonus is",bonus)