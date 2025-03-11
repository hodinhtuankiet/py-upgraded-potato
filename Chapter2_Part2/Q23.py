def Check_chan(x):
    if x % 2 == 0:
        print(x, "là số chẵn")
    else:
        print(x, "là số lẻ")

n = int(input("Nhập vào một số để kiểm tra: "))
Check_chan(n)
