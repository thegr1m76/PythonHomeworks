text = input("Enter a string: ")
symbol = input("Enter a symbol to replace vowels with: ")
vowels = "aeiouAEIOU"
replaced_text = ''.join(symbol if char in vowels else char for char in text)
print("Updated string:", replaced_text)