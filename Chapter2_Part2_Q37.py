words = []
while True:
    word = input("Enter a word (or press Enter to stop): ")
    if word == "":
        break
    if word not in words:
        words.append(word)

print("The unique words are:")
for word in words:
    print(word)
