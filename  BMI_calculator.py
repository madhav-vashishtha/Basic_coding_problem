'''BMI Calculator
Calculate BMI and display: Underweight, Normal, Overweight, Obese'''

weight=float(input("enter your weight in kg: "))
height=int(input("enter your height in meter: "))

bmi=weight/(height ** 2)

if bmi < 18.5:
    print("Categories: Underweight")
elif bmi < 25:
    print("Categories: Normal")
elif bmi < 30:
    print("Categories: Overweight")
else:
    print("Categories: Obese")
