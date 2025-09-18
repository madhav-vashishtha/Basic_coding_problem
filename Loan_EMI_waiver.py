'''Loan EMI Waiver
If ≥12 EMIs paid without delay, waive 1 EMI.'''
emi=int(input("enter number of emi paid without delay: "))
def loan_emi_waiver(emi):
    if emi>=12:
        print("eligible for emi waiver")
    else:
        print("NOT eligible for emi wavier")
loan_emi_waiver(emi)
