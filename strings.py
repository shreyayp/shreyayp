# Define a sample string
sample_string = "Hello, World!"

# 1. len(): Returns the length of the string
print("Length of the string:", len(sample_string))

# 2. capitalize(): Capitalizes the first character of the string
print("Capitalized string:", sample_string.capitalize())

# 3. upper(): Converts all characters to uppercase
print("Uppercase string:", sample_string.upper())

# 4. lower(): Converts all characters to lowercase
print("Lowercase string:", sample_string.lower())

# 5. title(): Converts the first character of each word to uppercase
print("Titlecased string:", sample_string.title())

# 6. count(): Returns the number of occurrences of a substring in the string
print("Number of 'l's in the string:", sample_string.count('l'))

# 7. find(): Returns the index of the first occurrence of a substring in the string
print("Index of 'World' in the string:", sample_string.find('World'))

# 8. replace(): Replaces all occurrences of a substring with another substring
print("Replacing 'World' with 'Universe':", sample_string.replace('World', 'Universe'))

# 9. strip(): Removes leading and trailing whitespace characters
whitespace_string = "  Hello, World!  "
print("Stripped string:", whitespace_string.strip())

# 10. startswith(): Checks if the string starts with a specified prefix
print("Starts with 'Hello':", sample_string.startswith('Hello'))

# 11. endswith(): Checks if the string ends with a specified suffix
print("Ends with 'World!':", sample_string.endswith('World!'))
