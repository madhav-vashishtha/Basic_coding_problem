'''Character Classifier
Input character and classify: Vowel, Consonant, Digit, or Symbol.'''

ch = input("Enter a character: ")

if ch.isdigit():
    print("Digit")
elif ch.isalpha():
    if ch.lower() in 'aeiou':
        print("Vowel")
    else:
        print("Consonant")
else:
    print("Symbol")
