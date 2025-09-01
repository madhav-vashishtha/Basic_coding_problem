numbers = [18, 7, 45, 20, 35, 25]
largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num
print("Largest element is:",largest)
