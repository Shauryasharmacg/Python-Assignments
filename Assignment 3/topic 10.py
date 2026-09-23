# Q54. String and Integer
# Error: age is a string; cannot add string and integer.
age_fixed = int(input("Enter age: "))
print("Age after 5 years:", age_fixed + 5)

# Q55. Incorrect Quotes
# Error: Unescaped single quote ends string prematurely.
print("It's Python")  # or print('It\'s Python')

# Q56. Incorrect Slicing Syntax
# Error: Slicing uses colons (:), not commas (,).
text_slice = "Python"
print(text_slice[1:4])

# Q57. Incorrect split() Separator
# Error: .split(',') looks for a comma, but input has a space.
a_fixed, b_fixed = input().split()

# Q58. String Addition vs Numeric Addition
# Program prints: 1020 (string concatenation)
# Fix:
num_a, num_b = input().split()
print(int(num_a) + int(num_b))

# Q59. Escape Sequence Debugging
# Problem: \n and \t act as newline and tab escape sequences.
# Fix:
print("C:\\new\\test")  # or print(r"C:\new\test")