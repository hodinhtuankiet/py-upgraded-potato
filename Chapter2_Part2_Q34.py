decimal = int(input("Enter a decimal number: "))
binary = bin(decimal)[2:]  # Dùng hàm bin() và bỏ tiền tố '0b'

print(f"The binary representation of {decimal} is {binary}.")
