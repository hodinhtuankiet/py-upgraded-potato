numbers = []
while True:
    num = int(input("Enter an integer (or 0 to stop): "))
    if num == 0:
        break
    numbers.append(num)

numbers.sort()

print("The numbers in ascending order are:")
for num in numbers:
    print(num)
