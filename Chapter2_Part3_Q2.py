filename = 'alice.txt'

try:
    with open(filename) as f_obj:  # Mở file và tạo đối tượng f_obj
        contents = f_obj.read()  # Đọc và lưu nội dung file vào biến contents
except FileNotFoundError:  # Xử lý ngoại lệ khi không mở được file
    msg = "File " + filename + " không tồn tại."
    print(msg)
else:  # Trường hợp đọc file hợp lệ
    words = contents.split()  # Tách các từ trong nội dung lưu vào danh sách words
    num_words = len(words)  # Đếm số lượng từ trong danh sách words
    print("File " + filename + " có " + str(num_words) + " từ.")
