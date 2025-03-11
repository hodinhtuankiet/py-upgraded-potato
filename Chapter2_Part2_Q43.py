def compare_strings(str1, str2):
    if len(str1) > len(str2):
        print(str1)
    elif len(str1) < len(str2):
        print(str2)
    else:
        print(str1)
        print(str2)

string1 = input("Enter first string: ")
string2 = input("Enter second string: ")

compare_strings(string1, string2)
