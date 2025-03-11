import math

def tinh_chi_so_gio_lanh():
  """
  Tính toán chỉ số gió lạnh (WCI).
  """

  try:
    T = float(input("Nhập nhiệt độ không khí (°C): "))
    V = float(input("Nhập tốc độ gió (km/giờ): "))

    WCI = 13.12 + 0.6215 * T - 11.37 * (V ** 0.16) + 0.3965 * T * (V ** 0.16)

    WCI_rounded = round(WCI)

    print(f"\nChỉ số gió lạnh (WCI): {WCI_rounded}")

  except ValueError:
    print("Vui lòng nhập số hợp lệ.")

if __name__ == "__main__":
  tinh_chi_so_gio_lanh()