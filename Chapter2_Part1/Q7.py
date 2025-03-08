import math


a = float(input("Nhập cạnh a: "))
b = float(input("Nhập cạnh b: "))
C = float(input("Nhập góc C (radian): ")) 


S = 0.5 * a * b * math.sin(C)


print(f"Diện tích tam giác là: {S:.2f}")
