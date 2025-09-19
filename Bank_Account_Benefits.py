'''Bank Account Benefits
Input account type (Savings, Current, Salary) and print benefits.'''

account_type = input("Enter account type (Savings, Current, Salary): ")

def account(type):
    if type == "Savings":
        print("Benefit: Safe place to keep money and earn interest.")
    elif type == "Current":
        print("Benefit: No transaction limits, Mainly for business people")
    elif type == "Salary":
        print("Benefit: Zero minimum balance requirement.")
    else:
        print("Invalid account type.")
account(account_type)