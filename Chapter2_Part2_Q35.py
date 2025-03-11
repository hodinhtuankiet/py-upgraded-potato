numbers = input("Enter numbers separated by commas: ").split(',')
numbers = [int(num) for num in numbers]

odd_numbers = [num for num in numbers if num % 2 != 0]

print("Odd numbers:", odd_numbers)
