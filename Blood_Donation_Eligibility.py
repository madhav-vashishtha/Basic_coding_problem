'''Blood Donation Eligibility
Eligible if age 18–60 and weight ≥50 kg.'''

age=int(input("enter your age: "))
weight=float(input("enter your weight in kg: "))

if age>=18 and age<=60 and weight>=50:
    print("eligible for blood donation")
else:
    print("NOT eligible for blood donation")
