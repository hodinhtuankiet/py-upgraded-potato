def is_palindrome(text):
    return text == text[::-1]

string = input("Enter a string to check if it's a palindrome: ")

if is_palindrome(string):
    print(f"'{string}' is a palindrome!")
else:
    print(f"'{string}' is not a palindrome.")
