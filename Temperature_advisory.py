'''Temperature Advisory
Input Celsius temperature:
< 0 → Freezing
0–20 → Cold
21–35 → Normal
36–45 → Hot
45 → Heatwave Alert'''

temp=int(input("enter temperature in celsius: "))

if temp<0:
    print("Freezing")
elif temp>0 and temp<20:
    print("Cold")
elif temp>21 and temp<35:
    print("Normal")
elif temp>36 and temp<45:
    print("Hot")
else:
    print("Heatwave Alert")
    