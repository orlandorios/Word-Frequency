import string

with open('one-today.txt', 'r') as file:
    text_string = file.read90.replace('\n', '')
    # convert string of words into a list
list_of_text = text_string.split('')

print(type(list_of_text))