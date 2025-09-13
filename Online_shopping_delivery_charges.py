order_amount=int(input("enter order amount: "))
prime= input("Are you a Prime Member? (yes/no): ")

if order_amount >=1000:
    print("Delivery charges: Free")
elif order_amount<1000 and prime == "yes":
    print("Delivery charges:  ₹20")
else:
    print("Delivery charges: ₹50")