import math

def tinh_toc_do_cham_dat():
  """
  Tính toán tốc độ của vật khi chạm đất.
  """

  try:
    d = float(input("Nhập chiều cao thả vật (mét): "))

    v_i = 0

    a = 9.8

    v_f = math.sqrt(v_i**2 + 2 * a * d)

    print(f"\nTốc độ khi chạm đất: {v_f:.2f} m/s")

  except ValueError:
    print("Vui lòng nhập số hợp lệ.")

if __name__ == "__main__":
  tinh_toc_do_cham_dat()