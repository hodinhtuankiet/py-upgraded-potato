import re

def is_good_password(password):
    if len(password) >= 8 and \
       re.search(r'[a-z]', password) and \
       re.search(r'[A-Z]', password) and \
       re.search(r'[0-9]', password):
        return True
    return False

# Nhập mật khẩu từ người dùng
password = input("Enter your password: ")

# Kiểm tra mật khẩu và hiển thị kết quả
if is_good_password(password):
    print("The password is good.")
else:
    print("The password is not good.")
