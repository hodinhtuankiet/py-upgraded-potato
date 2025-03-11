tuple_data = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

even_tuple = tuple(x for x in tuple_data if x % 2 == 0)

print(even_tuple)
