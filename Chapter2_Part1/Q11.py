
length = float(input("Nhập chiều dài của cánh đồng (mét): "))
width = float(input("Nhập chiều rộng của cánh đồng (mét): "))

area_square_meter = length * width

acre = 43560  
area_acre = area_square_meter / acre

print(f"Diện tích cánh đồng là: {area_acre:.4f} Mẫu Anh")
