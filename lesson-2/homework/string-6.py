string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

if string2 in string1 or string2 in string1:
    print(f'"{string1}" contains "{string2}".')
else:
    print(f'"{string1}" does not contain "{string2}".')