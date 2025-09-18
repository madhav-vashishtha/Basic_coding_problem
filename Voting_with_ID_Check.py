'''Voting with ID Check
Allow voting if age ≥18 and has valid ID'''

age=int(input("enter your age:"))
if age>=18:
    print("Eliqible to vote")
else:
    print("Not Eliqible")