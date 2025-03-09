ftext = open("romeo.txt")  # Mở file romeo.txt
tu_dien_cac_tu = {}  # Dictionary để lưu tần suất từ

# Đọc từng dòng trong file
for dong in ftext:
    danh_sach_tu = dong.split()  # Tách các từ trong dòng
    for tu in danh_sach_tu:
        tu_dien_cac_tu[tu] = tu_dien_cac_tu.get(tu, 0) + 1  # Đếm số lần xuất hiện của từ

# Chuyển đổi dictionary thành danh sách tuple (tần suất, từ)
danh_sach = []
for key, val in tu_dien_cac_tu.items():
    newtup = (val, key)  
    danh_sach.append(newtup)

# Sắp xếp danh sách theo tần suất giảm dần
danh_sach = sorted(danh_sach, reverse=True)

# In ra 10 từ xuất hiện nhiều nhất
for val, key in danh_sach[:10]:
    print(key, val)
