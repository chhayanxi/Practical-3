# Define a string
original_string = "Hello, World!"

# Reverse the string
reversed_string = original_string[::-1]

# Replace string with another string
replaced_string = original_string.replace("World", "Python")

# Merge two strings
string1 = "Hello"
string2 = "Python"
merged_string = string1 + " " + string2

# Check if a character is in the string without using loops
character_to_find = "l"
is_character_present = character_to_find in original_string

# Split string into multiple words & characters
words = original_string.split()
characters = list(original_string)

# Display the results
print("Original String:", original_string)
print("Reversed String:", reversed_string)
print("String after replacement:", replaced_string)
print("Merged String:", merged_string)
print("Is '{}' present in the original string? {}".format(character_to_find, is_character_present))
print("Words from the original string:", words)
print("Characters from the original string:", characters)
