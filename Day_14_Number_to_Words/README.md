# Day 14: Number to Words 🔢➡️📝

## Project Overview
Convert any number from 1 to 999 into its English word representation.

## Challenge
**Difficulty:** Medium

Write a program that takes a number (1-999) and converts it to words.

### Examples
Input: 247
Output: "two hundred forty seven"

Input: 19
Output: "nineteen"

Input: 500
Output: "five hundred"

Input: 83
Output: "eighty three"


## Learning Objectives
- Work with dictionaries for mapping
- Practice string concatenation
- Understand modular arithmetic (division and remainder)
- Break down problems into smaller parts

## Approach Hints

### Step 1: Create Your Dictionaries
ones = {1: "one", 2: "two", ..., 19: "nineteen"}
tens = {20: "twenty", 30: "thirty", ..., 90: "ninety"}


### Step 2: Break Down the Number
- **Hundreds place:** `num // 100`
- **Remainder:** `num % 100`

### Step 3: Build the String
1. Handle hundreds digit
2. Handle tens and ones (watch for 11-19!)

## Tips
- Handle special cases: 11-19 don't follow the tens+ones pattern
- Remember to add "hundred" after the hundreds digit
- Use spaces between words
- Test edge cases: 100, 101, 111, 999

## Bonus Challenges
- Extend to handle numbers up to 999,999
- Add "and" in proper places (e.g., "two hundred and forty seven")
- Handle zero as a special case

Happy coding! 🚀