''' Grading System with Distinction
Percentage to grade:
≥ 90 → A+
75–89 → A
60–74 → B
50–59 → C
35–49 → D
< 35 → Fail
If ≥ 95 → Mention “Distinction”.
'''

percentage=int(input("enter your percentage: "))

if percentage>=95:
    print("Distinction")
elif percentage>=90:
    print("Grade:A+")
elif percentage>75 and percentage<89:
    print("Grade:A")
elif percentage>60 and percentage<74:
    print("Grade:B")
elif percentage>=50 and percentage<59:
    print("Grade:C")
elif percentage>35 and percentage<49:
    print("Grade:D")
else:
    print("Fail")

