def first_five_squares():
    squares = []
    for i in range(1, 21):
        squares.append(i ** 2)
    return squares

result = first_five_squares()
print(result[:5])  # In 5 phần tử đầu tiên
