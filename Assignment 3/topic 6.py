# Q24. Basic Slicing
# Output:
# PYT
# THO
# YTHON

# Q25. Start and Stop
# Output:
# PROG
# RAMMING
# PROGRAMMING

# Q26. Negative Slicing
# Output:
# PUTER
# COMPU
# OMPU

# Q27. Step in Slicing
# Output:
# PTO
# YHN
# NOHTYP

# Q28. Reverse a String
rev_str = input("Enter string: ")
print(rev_str[::-1])

# Q29. Alternate Characters
alt_str = input("Enter string: ")
print(alt_str[::2])

# Q30. Extract First and Last Three Characters
three_str = input("Enter string: ")
print(three_str[:3], three_str[-3:])

# Q31. Slicing Challenge
# text[2:8:2]  -> 'CEG'   (start: 2, stop: 8, step: 2)
# text[8:2:-2] -> 'IGE'   (start: 8, stop: 2, step: -2)
# text[::-2]   -> 'JHFDB' (start: -1 / end, stop: beginning, step: -2)

# Q32. Slice Without Counting from the Beginning
text_batch = "BTECH-CSE-2026"
print(text_batch[:5])
print(text_batch[6:9])
print(text_batch[-4:])