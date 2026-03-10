# Day 5: Word Reverser (Easy) 🔄

Welcome to Day 5! Today you're going to play with string manipulation and learn how to reverse words in fun ways.

## 📋 Task

Create a program that:
1. Takes a sentence as input
2. Reverses each word individually (but keeps them in the same order)
3. Also reverses the entire sentence (word order)
4. Shows both results

## 🎯 Example

**Input:** `"Hello World Python"`

**Output:**
Reversed words: olleH dlroW nohtyP
Reversed sentence: Python World Hello


## 💡 Key Concepts

You'll use these Python string methods:

- **`sentence.split()`** - Splits a sentence into a list of words
  
  "Hello World".split()  # Returns: ['Hello', 'World']
  


- **`word[::-1]`** - Reverses a string using slicing
  
  "Hello"[::-1]  # Returns: 'olleH'
  


- **`' '.join(words)`** - Joins a list of words back into a sentence
  
  ' '.join(['Hello', 'World'])  # Returns: 'Hello World'
  


## 🚀 Getting Started

1. Ask the user for a sentence
2. Split it into words
3. Reverse each word (hint: use a loop or list comprehension!)
4. Join them back together
5. For the sentence reversal, reverse the *order* of words

## ✨ Bonus Challenges

- Handle punctuation gracefully
- Let the user enter multiple sentences
- Create a function that can do both types of reversal

Good luck, and have fun reversing! 🎉