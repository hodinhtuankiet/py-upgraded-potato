def remove_first_five_squares():
    squares = [i ** 2 for i in range(1, 21)]
    return squares[5:]

result = remove_first_five_squares()
print(result)
