# Step 1: Vowels Dictionary
vowel_counts = {'a': 0, 'e':0, 'i':0, 'o':0, 'u':0}
consonants = []

# Step 2: User Input
sent = input("Enter a sentence:\n")

# Step 3: For loop for char 
for char in sent:
    lower_case_char = char.lower()

# Step 4: Increments vowels
    if lower_case_char in vowel_counts:
        vowel_counts[lower_case_char] += 1
    elif lower_case_char.isalpha() and lower_case_char not in vowel_counts:
        consonants.append(lower_case_char)
    
# Step 5: Result
print("---------------Result----------------")
for key, value in vowel_counts.items():
    print(f"{key}: {value} time in the sentence.")
print(f"There are total of {len(consonants)} consonants in this sentence.")