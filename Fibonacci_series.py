#Fibonacci series ek number sequence hai jisme:
#Pehle 2 numbers fix hote hain: 0 aur 1
#Har agla number apne pehle do numbers ka sum hota hai.
a=0
b=1
for i in range(10):
    print(a, end="")
    a, b = b, a+b