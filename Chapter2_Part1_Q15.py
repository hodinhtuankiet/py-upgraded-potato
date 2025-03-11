def tinh_nang_luong_va_chi_phi():
  """
  Tính toán năng lượng và chi phí để làm nóng nước.
  """
  try:
    M = float(input("Nhập khối lượng nước (gram): "))
    delta_T = float(input("Nhập độ thay đổi nhiệt độ (°C): "))

    C = 4.186

    Q = M * C * delta_T

    Q_kWh = Q * 2.777e-7

    chi_phi = Q_kWh * 8.9

    print(f"\nNăng lượng cần thiết: {Q:.2f} Joules")
    print(f"Chi phí điện năng: {chi_phi:.2f} cent")

  except ValueError:
    print("Vui lòng nhập số hợp lệ.")

if __name__ == "__main__":
  tinh_nang_luong_va_chi_phi()