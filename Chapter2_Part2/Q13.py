lines = []
while True:
   s = input("Enter a string: ")
   if s:
      lines.append(s.upper())
   else:
      break;
for sentence in lines:
    print(sentence)
