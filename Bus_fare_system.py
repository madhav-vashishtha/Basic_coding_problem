age=int(input("Enter passenger age: "))
ticket_price=float(input("Enter ticket price:" ))

if age <= 5:
    fare = 0
elif age >5 and age <=17:
    fare = ticket_price / 2
elif age >=18 and age <=60:
    fare = ticket_price 
else:
    fare = ticket_price * 0.75
print("Final payable fare: ", fare)
