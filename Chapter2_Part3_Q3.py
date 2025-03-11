def count_words(filename):  # Định nghĩa hàm count_words()
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = "File " + filename + " không tồn tại."
        print(msg)
    else:
        words = contents.split()  # Tách các từ trong nội dung
        num_words = len(words)  # Đếm số từ
        print("File " + filename + " có " + str(num_words) + " từ.")

# Danh sách các tệp cần kiểm tra
filenames = ['f1.txt', 'f2.txt', 'f3.txt']

# Lặp qua từng tệp trong danh sách và gọi hàm count_words
for filename in filenames:
    count_words(filename)
