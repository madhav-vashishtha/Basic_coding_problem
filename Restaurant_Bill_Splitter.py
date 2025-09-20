'''Restaurant Bill Splitter
If friends ≥4, give 10% discount, else full bill.'''

bill = float(input("Enter total bill amount: "))
friends = int(input("Enter number of friends: "))

if friends >= 4:
    bill = bill * 0.9

per_person = bill / friends
print("Final Bill: ₹", bill)
print("Each person pays: ₹", (per_person))