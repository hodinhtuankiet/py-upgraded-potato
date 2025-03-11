from tu_dien import *

max = int(input("Nhap chi so Max: "))  # Thêm dấu đóng ngoặc
TD = tao_TD(max)

print("Cac phan tu của tu dien la:")
Print_Item(TD)

print("Khoa các phan tu của tu dien:")
Print_key(TD)

print("Gia tri các phan tu của tu dien:")
Print_value(TD)
