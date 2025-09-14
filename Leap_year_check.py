'''Leap Year Check
Check leap year using divisible by 400, 
or divisible by 4 but not by 100.'''

year=int(input("enter a year: "))

if (year%400 == 0) or (year%4 == 0 and year%100 != 0):
    print(year,"is a Leap Year")
else:
    print(year,"is NOT a Leap Year")