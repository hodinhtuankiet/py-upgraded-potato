def caesar_cipher(text, shift):
    result = ""

    for char in text:
        if char.isalpha():  # Kiểm tra nếu ký tự là chữ cái
            start = ord('A') if char.isupper() else ord('a')
            result += chr(start + (ord(char) - start + shift) % 26)
        else:
            result += char  # Ký tự không phải chữ cái thì giữ nguyên

    return result

def decode_caesar_cipher(text, shift):
    return caesar_cipher(text, -shift)

action = input("Do you want to encode or decode? (Enter 'encode' or 'decode'): ").lower()
message = input("Enter your message: ")
shift = int(input("Enter the number of positions to shift: "))

if action == 'encode':
    encoded_message = caesar_cipher(message, shift)
    print(f"Encoded message: {encoded_message}")
elif action == 'decode':
    decoded_message = decode_caesar_cipher(message, shift)
    print(f"Decoded message: {decoded_message}")
else:
    print("Invalid action. Please enter 'encode' or 'decode'.")
