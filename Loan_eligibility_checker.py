'''Loan Eligibility Checker
Eligible if salary ≥ 25,000 and CIBIL ≥ 700.'''

salary=float(input("enter your salary:"))
cibil=int(input("enter your cibil: "))

def loan_eligibility(salary, cibil):
    if salary>=25000 and cibil>=700:
        return "Eligible for loan"
    else:
        return "NOT Eligible for loan"
print(loan_eligibility(salary, cibil))