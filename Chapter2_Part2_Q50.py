import random

def generate_random_password():
    length = random.randint(7, 10)
    password = ''.join(chr(random.randint(33, 126)) for _ in range(length))
    return password

# Tạo và hiển thị mật khẩu ngẫu nhiên
password = generate_random_password()
print("Generated password:", password)
