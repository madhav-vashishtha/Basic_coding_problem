amount=int(input("enter the amount to withdrawl: "))

if amount%100==0:
    print(f"Withdrawal of ₹{amount} successful.")
else:
    print("Error: Amount must be a multiple of 100.")
