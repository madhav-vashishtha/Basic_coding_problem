''' Marks Evaluation
Print performance: Excellent (≥90), Good (70–89), 
Average (50–69), Poor (<50).'''

marks=int(input("enter the marks: "))

if marks>=90:
    print("Excellent")
elif marks>70 and marks<89:
    print("Good")
elif marks>50 and marks<69:
    print("Average")
else:
    print("Poor")
    