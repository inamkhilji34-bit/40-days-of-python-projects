import string
# A program to check the strength of a Password:
# User Input
print("A strong password has the following 5 characters:\n1.Length greater than 8.\n2.Has Upper Character.\n3.Has Lower Character.\n4.Has Digit\n5.Has Special Characters.")
password = input("Enter a password: ")

has_upper = any(c.isupper() for c in password)
has_lower = any(c.islower() for c in password)
has_digit = any(c.isdigit() for c in password)
has_char = any(c in string.punctuation for c in password)
has_length = len(password) >= 8

# Score
score = sum([has_char, has_digit, has_length, has_lower, has_upper])
print(f"Password Strength: {score}/5")

if not has_length:
    print("Missing: Minimum 8 characters required.")
if not has_lower:
    print("Missing: Lower characters.")
if not has_upper:
    print("Missing: Upper Characters.")
if not has_digit:
    print("Missing: Digits.")
if not has_char:
    print("Missing: Special Characters.")
if score == 5:
    print("Congragulations, Your password is strong.")
