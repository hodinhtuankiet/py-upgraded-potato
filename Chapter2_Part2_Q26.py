letter = input("Enter a letter: ").lower()

if letter in ['a', 'e', 'i', 'o', 'u']:
    print("The letter you entered is a vowel.")
elif letter == 'y':
    print("The letter 'y' can be a vowel or a consonant.")
else:
    print("The letter you entered is a consonant.")
