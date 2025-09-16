'''Mobile Data Usage Warning
If daily data usage > plan limit, display warning.'''

plan_limit=float(input("enter your daily data limit (in GB): "))
usage=float(input("enter today's data usage (in GB): "))

if usage > plan_limit:
    print("Warning: You have exceeded your daily data limit!")
else:
    print("You are within your daily data limit.")