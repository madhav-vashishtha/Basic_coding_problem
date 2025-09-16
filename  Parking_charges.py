'''Parking Charges
Free for 2 hours, ₹20/hr (3–5 hrs), ₹50/hr (after 5 hrs).'''

hour=int(input("enter hour: "))

if hour<=2:
    print("Free")
elif hour>=3 and hour<=5:
    charge=hour*20
    print("charges of parking is",charge)
else:
    charge=hour*50
    print("charge of parking is",charge)
    