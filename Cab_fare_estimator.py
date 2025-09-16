'''Cab Fare Estimator
Base fare + per km charge. If time ≥ 10PM, add night surcharge.'''

base_fare = 50         
per_km = 12            
distance = int(input("Enter distance travelled (in km): "))
time = int(input("Enter time in 24-hour format (e.g. 22 for 10 PM): "))

fare = base_fare + (per_km * distance)

if time >= 22:
    fare += 30  

print("Total Cab Fare =", fare)
