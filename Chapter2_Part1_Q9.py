import math

a = float(input("Nhập cạnh tam giác đều a: "))
# CT Heron (tam giác đều)
s = (3 * a) / 2  # Nửa chu vi của tam giác đều
S_heron = math.sqrt(s * (s - a) * (s - a) * (s - a))

# CT cho tam giác đều
S_simple = (math.sqrt(3) / 4) * a ** 2

print(f"Diện tích tam giác đều theo định lý Heron: {S_heron:.2f}")
print(f"Diện tích tam giác đều theo công thức đơn giản: {S_simple:.2f}")
