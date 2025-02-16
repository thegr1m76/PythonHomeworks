text = input("Enter a string: ")
start_word = input("Enter the starting word: ")
end_word = input("Enter the ending word: ")

if text.startswith(start_word) and text.endswith(end_word):
    print("The string starts with '{}' and ends with '{}'.".format(start_word, end_word))
else:
    print("The string does not match the given conditions.")