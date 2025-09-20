'''Hostel Room Allocation
Allocate hostel based on gender: Male → Boys Hostel,
Female → Girls Hostel.'''

gender=input("enter your gender: ")

def Hostel_Room_Allocation(gender):
    if gender=="male":
        print("Boys hostel")
    else:
        print("Girls hostal")
Hostel_Room_Allocation(gender)