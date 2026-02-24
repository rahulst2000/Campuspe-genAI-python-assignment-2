# First it asks them to type in a line of text.
# how many characters are in the line,
# splitting text and counting the number of words
# converts all letters to uppercase
# converting all letters to lowercase.

text = input("Enter text: ")
print("Length:", len(text))
print("Words:", len(text.split()))
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
