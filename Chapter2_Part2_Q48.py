def average(a, b, c):
    return (a + b + c) / 3

# Nhập ba giá trị từ người dùng
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

# Tính và hiển thị giá trị trung bình
avg = average(num1, num2, num3)
print("The average is:", avg)
