income= int(input("enter the income: "))

if income<=250000:
    tax=0
elif income>=250001 and income<=500000:
    tax=0.05*250000
elif income>=500001 and income<=1000000:
    tax =0.20*(500000)+12500
else:
    tax=0.30*(1000000)+112500

print("tax",tax)