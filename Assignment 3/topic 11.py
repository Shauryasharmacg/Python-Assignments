# Q60. Student Result Information
st_name = input("Name: ")
m1, m2, m3 = input("Marks: ").split()
tot = int(m1) + int(m2) + int(m3)
avg = tot / 3
print(f"Name: {st_name}")
print(f"Total: {tot}")
print(f"Average: {avg:.2f}")

# Q61. Student ID Analyzer
full_id = input("Enter ID: ")
deg, batch_yr, br, r_str = full_id.split("-")
roll_num = int(full_id[-3:])
print(f"Degree: {deg}")
print(f"Batch: {batch_yr}")
print(f"Branch: {br}")
print(f"Roll Number: {roll_num}")

# Q62. Username Generator
name_three = input("Enter full name: ")
w_first, w_mid, w_last = name_three.split()
username_gen = w_first.lower() + "." + w_last.lower()
print(username_gen)

# Q63. Sentence Information
sen_input = input("Enter sentence: ")
words_all = sen_input.split()
print("First word:", words_all[0])
print("Last word:", words_all[-1])
print("Total words:", len(words_all))

# Q64. Email Analyzer + Membership
em_input = input("Enter email: ")
at_present = "@" in em_input
em_user, em_domain = em_input.split("@")
print(f"@ Present: {at_present}")
print(f"Username: {em_user}")
print(f"Domain: {em_domain}")

# Q65. Character Analyzer
single_char = input("Enter character: ")
char_code = ord(single_char)
print(f"Character: {single_char}")
print(f"Code: {char_code}")
print(f"Previous: {chr(char_code - 1)}")
print(f"Next: {chr(char_code + 1)}")

# Q66. Product Bill
prod_name = input("Product: ")
p_price = float(input("Price: "))
p_qty = int(input("Quantity: "))
p_disc = float(input("Discount: "))
sub_tot = p_price * p_qty
disc_amt = sub_tot * p_disc / 100
fin_tot = sub_tot - disc_amt
print(f"Product: {prod_name}")
print(f"Price: {p_price:.2f}")
print(f"Quantity: {p_qty}")
print(f"Subtotal: {sub_tot:.2f}")
print(f"Discount: {disc_amt:.2f}")
print(f"Final Total: {fin_tot:.2f}")

# Q67. Date Analyzer
date_raw = input("Enter date: ")
d_day, d_month, d_year = date_raw.split("-")
print(f"Day: {d_day}")
print(f"Month: {d_month}")
print(f"Year: {d_year}")
print(date_raw[-4:])

# Q68. String Transformation Challenge
str_two = input("Enter two words: ")
word_one, word_two = str_two.split()
print(f"First Word: {word_one}")
print(f"Second Word: {word_two}")
print(f"First Word Reversed: {word_one[::-1]}")
print(f"Second Word Reversed: {word_two[::-1]}")

# Q69. Final Challenge — Student Code Formatter
id_code_in = input("Enter ID: ")
c_deg, c_batch, c_branch, c_roll = id_code_in.split("-")
code_str = f"{c_deg}/{c_branch}/{c_roll}"
print(f"Degree: {c_deg}")
print(f"Batch: {c_batch}")
print(f"Branch: {c_branch}")
print(f"Roll: {c_roll}")
print(f"Code: {code_str}")

# Q70. Final String + Input/Output Challenge
orig_full_name = input("Enter full name: ")
name_parts = orig_full_name.split()
f_part = name_parts[0]
l_part = name_parts[-1]
f_up = f_part[:3].upper()
l_low = l_part[1:4].lower()
rev_name = orig_full_name[::-1]

print(f"Original: {orig_full_name}")
print(f"First Name: {f_part}")
print(f"Last Name: {l_part}")
print(f"First Name (Upper Part): {f_up}")
print(f"Last Name (Lower Part): {l_low}")
print(f"Full Name Reversed: {rev_name}")