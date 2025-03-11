def format_list(words):
    if len(words) == 1:
        return words[0]
    elif len(words) == 2:
        return ' and '.join(words)
    else:
        return ', '.join(words[:-1]) + ' and ' + words[-1]

# Nhập danh sách từ
words = input("Enter words separated by commas: ").split(', ')

# Định dạng và hiển thị kết quả
formatted_words = format_list(words)
print("Formatted list:", formatted_words)
