# Day 7: Vowel Counter (Easy)

## 📝 Task Description
Create a program that counts how many times each vowel (a, e, i, o, u) appears in a sentence. The program should show a breakdown of each vowel's count, not just the total number of vowels.

## 🎯 Learning Objectives
- Working with dictionaries in Python
- String manipulation and iteration
- Using the `.lower()` method for case-insensitive comparisons
- Conditional logic with `if` statements

## 💡 Hints
- Create a dictionary with vowel keys (a, e, i, o, u) and initialize counts to 0
- Loop through each character in the sentence
- Check if `char.lower()` is in your vowel dictionary
- If yes, increment that vowel's count

## 📋 Example Output
Enter a sentence: Hello World
Vowel breakdown:
a: 0
e: 1
i: 0
o: 2
u: 0


## 🚀 Getting Started

### Basic Structure
# Initialize vowel counts
counts = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

# Get input from user
sentence = input("Enter a sentence: ")

# Your code here to count vowels

# Display results


## ✨ Bonus Challenges
1. Add a total count at the end
2. Show which vowel appeared most frequently
3. Calculate the percentage of each vowel

## 🤔 Common Pitfalls
- Forgetting to use `.lower()` - "A" and "a" should both be counted
- Not initializing all vowels in the dictionary - what if a vowel doesn't appear?
- Trying to count the total instead of breaking down by each vowel

Happy coding! 🎉