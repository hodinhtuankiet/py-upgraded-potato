negatives = []
zeros = []
positives = []

while True:
    try:
        num = input("Enter an integer (or press Enter to stop): ")
        if num == "":
            break
        num = int(num)
        if num < 0:
            negatives.append(num)
        elif num == 0:
            zeros.append(num)
        else:
            positives.append(num)
    except ValueError:
        print("Please enter a valid integer.")

# Concatenate lists: negatives, zeros, positives
result = negatives + zeros + positives

print("The numbers in the required order are:")
for number in result:
    print(number)
