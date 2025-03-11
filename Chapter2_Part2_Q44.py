def squares_list():
    squares = []
    for i in range(1, 21):
        squares.append(i ** 2)
    return squares

result = squares_list()
print(result)
