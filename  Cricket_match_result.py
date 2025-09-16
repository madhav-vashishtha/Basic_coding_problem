'''Cricket Match Result
Input runs of two teams and declare winner or tie'''

a = int(input("Enter runs for Team A: "))
b = int(input("Enter runs for Team B: "))

if a > b:
    print("Team A won by", a - b, "runs")
elif b > a:
    print("Team B won by", b - a, "runs")
else:
    print("Match tied")
