'''Scholarship Eligibility
Eligible if marks ≥85 and income < ₹2,00,000.'''

marks=int(input("enter your marks: "))
income=int(input("enter your income: "))

def Scholarship_Eligibility(marks, income):
    if marks>=85 and income<200000:
        print("eligible for scholarship")
    else:
        print("NOT eligibale for scholarship")
Scholarship_Eligibility(marks, income)