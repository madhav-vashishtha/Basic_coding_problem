'''Internet Speed Test
Speed categories: <2 = Slow, 2–10 = Average, 
10–50 = Fast, >50 = Superfast'''

speed=float(input("enter your internet speed in mbps: "))

def internet_speed_test(speed):
    if speed < 2:
        print("Speed Category: Slow")
    elif speed <= 10:
        print("Speed Category: Average")
    elif speed <= 50:
        print("Speed Category: Fast")
    else:
        print("Speed Category: Superfast")
internet_speed_test(speed)