num = int(input("Enter a number: "))
level = int(input("Bậc: "))

total = 0
temp = num

while temp > 0:
    digit = temp % 10
    total += digit ** level  # Dùng level thay vì bac
    temp //= 10

if num == total:
    print(num, "is an Armstrong number, level:", level)
else:
    print(num, "is not an Armstrong number")
