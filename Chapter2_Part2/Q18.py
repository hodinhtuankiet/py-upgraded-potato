chuoi = input("Nhập vào một chuỗi: ")

# Khởi tạo dictionary đúng cú pháp
d = {"chu_hoa": 0, "chu_thuong": 0}  

for ch in chuoi:
    if ch.isupper():  # Không cần so sánh == True
        d["chu_hoa"] += 1
    elif ch.islower():
        d["chu_thuong"] += 1

print("Số chữ hoa là:", d["chu_hoa"])
print("Số chữ thường là:", d["chu_thuong"])
