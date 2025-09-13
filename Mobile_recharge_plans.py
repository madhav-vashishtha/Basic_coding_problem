'''Mobile Recharge Plans
Recharge packs:

₹199 → 28 days, 1.5GB/day

₹399 → 56 days, 2GB/day

₹599 → 84 days, 3GB/day
Invalid input → Show “Invalid Plan”.
'''
recharge_packs=int(input("enter recharge packs:  "))

if recharge_packs==199:
    print("28 days, 1.5GB/days")
elif recharge_packs==399:
    print("56 days, 2GB/day")
elif recharge_packs==599:
    print("84 days, 3GB/day")
else:
    print("invalid plan")