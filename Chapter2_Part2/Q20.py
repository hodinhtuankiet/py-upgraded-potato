x = int(input("Nhập số cần tính giai thừa: "))

def giaithua(n):
    if n < 0:
        return "Không có giai thừa cho số âm!"
    elif n == 0 or n == 1:
        return 1
    else:
        return n * giaithua(n - 1)

print(f"Giai thừa của {x} là: {giaithua(x)}")
