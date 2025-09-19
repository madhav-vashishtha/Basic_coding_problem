'''Fuel Station Discount
If fuel ≥20 liters, give 5% discount.'''

liters=float(input("Enter Petrol in litres: "))

def Fuel_station_discount(liters):
    if liters>=20:
        rate=liters*94
        discount=rate-(rate*0.05)
        print("Amount:",discount)
    else:
        print("Amount:",(liters*94))
Fuel_station_discount(liters)
