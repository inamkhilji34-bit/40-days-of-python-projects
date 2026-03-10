# 📊 Day 4: Multiplication Table Generator

A simple Python program that displays a beautifully formatted multiplication table for any number you choose!

## 🎯 What This Program Does

This program asks you for a number and displays its complete multiplication table from 1 to 10 in a neat, aligned format.

### Example Output:
Enter a number: 7

7 x  1 =  7
7 x  2 = 14
7 x  3 = 21
7 x  4 = 28
7 x  5 = 35
7 x  6 = 42
7 x  7 = 49
7 x  8 = 56
7 x  9 = 63
7 x 10 = 70


## 🚀 How to Run

1. Make sure you have Python installed (version 3.6 or higher)
2. Save the code in a file called `multiplication_table.py`
3. Open your terminal/command prompt
4. Navigate to the folder containing the file
5. Run: `python multiplication_table.py`

## 💡 What You'll Learn

- Using `input()` to get user data
- Working with `for` loops and `range()`
- String formatting with f-strings
- Text alignment using `.rjust()` method
- Creating clean, readable output

## 🔧 Key Concepts

**Loop Structure:**
for i in range(1, 11):  # Creates numbers 1 through 10
    print(f'{n} x {i} = {n*i}')


**Alignment Trick:**
str(i).rjust(2)  # Right-aligns the number in 2 spaces


## 🎨 Challenge Extensions

Once you've mastered the basics, try these:
- Let users choose the range (not just 1-10)
- Display multiple tables side by side
- Add color to the output
- Save the table to a text file

## 📝 Notes

This is a beginner-friendly project perfect for practicing loops and formatting. Have fun! 🎉