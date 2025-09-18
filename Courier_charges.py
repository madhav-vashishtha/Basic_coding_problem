'''Courier Charges
Charges: ≤1kg = ₹50, 1–5kg = ₹100,
 5–10kg = ₹200, >10kg = Not Allowed.'''

weight =float(input("Enter weight in kg: "))

def courier_charges(weight):
    if weight <= 1:
        print("Courier Charge: ₹50")
    elif weight <= 5:
        print("Courier Charge: ₹100")
    elif weight <= 10:
        print("Courier Charge: ₹200")
    else:
        print("NOT allowed")
courier_charges(weight)