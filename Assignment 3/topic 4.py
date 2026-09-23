# Q12. Find Character Codes
print(ord("A"))  # 65
print(ord("a"))  # 97
print(ord("Z"))  # 90
print(ord("z"))  # 122
print(ord("0"))  # 48
print(ord("9"))  # 57
print(ord("@"))  # 64

# Q13. Convert Codes to Characters
print(chr(65))  # A
print(chr(66))  # B
print(chr(97))  # a
print(chr(98))  # b
print(chr(48))  # 0
print(chr(57))  # 9
print(chr(64))  # @

# Q14. Uppercase and Lowercase
# 1. ord("a") is larger (97 > 65)
# 2. Difference is 32 (97 - 65 = 32)
# 3. Yes, diff between ord("b") and ord("B") is also 32 (98 - 66 = 32)

# Q15. Character Code Program
ch = input("Enter a character: ")
print(ord(ch))

# Q16. Next Character
char_in = input("Enter an uppercase letter: ")
print(chr(ord(char_in) + 1))

# Q17. Character Comparison and Unicode
# Output:
# True
# True
# True
# True
# Reason: Characters are compared by Unicode points (ord('A')=65 < ord('B')=66, etc.)

# Q18. Unicode Character Challenge
print(chr(9731))  
print(chr(9829))  
print(chr(8377))  
print(ord("☃️"))   
print(ord("♥️"))   
print(ord("₹"))   