'''Weather Advisory System
If temperature <10 and raining → “Carry umbrella & warm clothes”.
Else → Normal message.'''

temp=int(input("enter temperature in celsius: "))
weather=input("enter weather: ")
def Weather_Advisory_System(temp,weather):
    if temp<10 and weather=="raining":
        print("Carry umbrella & warm clothes")
    else:
        print("Normal")
Weather_Advisory_System(temp,weather)