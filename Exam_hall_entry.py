'''Exam Hall Entry
Allow only if hall ticket and ID card both are valid.'''

hall_ticket=input("Is hall ticket valid?(yes/no): ")
id_card=input("Is id card valid?(yes/no): ")

if hall_ticket=="yes" and id_card=="yes":
    print("Entry allowed")
else:
    print("Entry NOT allowed")

