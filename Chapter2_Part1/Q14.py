import math

def calculate_and_display():
  try:
    a = int(input("Nhập số nguyên a: "))
    b = int(input("Nhập số nguyên b: "))

    print("\nKết quả:")
    print(f"Tổng của a và b: {a + b}")
    print(f"Hiệu của a và b: {a - b}")
    print(f"Tích của a và b: {a * b}")

    if b != 0:
      print(f"Thương của a chia cho b: {a / b}")
      print(f"Phần còn lại khi a được chia cho b: {a % b}")
    else:
      print("Không thể chia cho 0.")

    if a > 0:
      print(f"Kết quả của log10(a): {math.log10(a)}")
    else:
      print("Không thể tính logarit của số không dương.")

    print(f"Kết quả của a^b: {a ** b}")

  except ValueError:
    print("Vui lòng nhập số nguyên hợp lệ.")

if __name__ == "__main__":
  calculate_and_display()