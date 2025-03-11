def caesar_cipher(text, shift=3):
    result = ""

    for char in text:
        if char.isalpha():  # Kiểm tra nếu ký tự là chữ cái
            start = ord('A') if char.isupper() else ord('a')
            result += chr(start + (ord(char) - start + shift) % 26)
        else:
            result += char  # Ký tự không phải chữ cái thì giữ nguyên

    return result

message = input("Enter a message to encode: ")
encoded_message = caesar_cipher(message, 3)
print(f"Encoded message: {encoded_message}")
