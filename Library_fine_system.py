days_late = int(input("Enter the number of late days: "))

if days_late <= 7:
    print("No fine")
elif days_late >= 8 and days_late <= 14:
    fine = days_late * 5
    print("Fine = ₹", fine)
elif days_late >= 15 and days_late <= 30:
    fine = days_late * 10
    print("Fine = ₹", fine)
else:
    print("Membership Cancelled")
