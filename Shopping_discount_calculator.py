bill=int(input("Enter total bill amount: "))

if bill>5000:
    discount=0.20*bill
elif bill<=2000 and bill>=5000:
    discount= 0.10*bill
else:
    discount=0

final_amount = bill -discount

print("Final Payable Amount: ₹", final_amount)
