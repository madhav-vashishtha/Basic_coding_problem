balance = int(input("Enter current balance: "))
withdraw = int(input("Enter withdrawal amount: "))

if withdraw > balance:
    print("Insufficient Balance")
elif withdraw % 100 != 0:
    print("Invalid Amount")
else:
    balance -= withdraw
    print("Transaction Successful")
    print("Remaining Balance:", balance)
