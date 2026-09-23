# Q33. Basic split()
# Output: ['Python', 'is', 'easy']
# Whitespace (spaces) separates the words by default.

# Q34. Custom Separator
# Output: ['apple', 'banana', 'mango']

# Q35. Separator Not Present
# Output: ['Python is easy']
# Reason: Comma ',' does not exist in the string, so no split occurs.

# Q36. Split a Full Name
full_name_input = input("Enter full name: ")
w1, w2, w3 = full_name_input.split()
print(w1)
print(w2)
print(w3)

# Q37. Multiple Inputs Using split()
first_name, last_name = input("Enter two names: ").split()
print("First Name:", first_name)
print("Last Name:", last_name)

# Q38. Three Numeric Inputs
n1, n2, n3 = input("Enter 3 integers: ").split()
print(int(n1) + int(n2) + int(n3))

# Q39. Student Record
record = input("Enter record: ")
name, age, course, city = record.split(",")
print("Name:", name)
print("Age:", age)
print("Course:", course)
print("City:", city)

# Q40. Email Analyzer
email_in = input("Enter email: ")
username, domain = email_in.split("@")
print("Username:", username)
print("Domain:", domain)

# Q41. Sentence Analyzer
sentence_in = input("Enter sentence: ")
words_list = sentence_in.split()
print("First word:", words_list[0])
print("Last word:", words_list[-1])
print("Total words:", len(words_list))