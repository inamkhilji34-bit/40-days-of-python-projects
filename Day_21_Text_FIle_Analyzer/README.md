# Day 21: Text File Analyzer 📄

Here's a clean README for your project!

---

# Day 21: Text File Analyzer

## 📋 Description
A Python program that reads a `.txt` file and generates a detailed
analysis report including word statistics, sentence count, most
frequent words, and estimated reading time.

## 🎯 Learning Goals
- Reading and processing text files in Python
- String manipulation and cleaning
- Using `collections.Counter` for word frequency
- Calculating text statistics

## 📁 Project Structure
day21_text_analyzer/
│
├── analyzer.py        # Main program
├── sample.txt         # Sample text file to analyze
└── README.md          # This file

## 🚀 How to Run
1. Make sure you have a `.txt` file ready (or use `sample.txt`)
2. Run the program:

   python analyzer.py

3. Enter the filename when prompted

## 📊 Features
- **Word Count** – Total number of words in the file
- **Sentence Count** – Estimated number of sentences
- **Top 5 Words** – Most frequently used words (excluding common words)
- **Average Word Length** – Mean number of characters per word
- **Reading Time** – Estimated time to read (based on 200 words/min)

## 💡 Key Concepts Used
- `open()` and `.read()` for file handling
- `.split()` and `.lower()` for text processing
- `collections.Counter` for word frequency
- f-strings for formatted output

## 🧪 Sample Output
========================================
       TEXT FILE ANALYSIS REPORT
========================================
File: sample.txt
----------------------------------------
Word Count:        342
Sentence Count:    24
Avg Word Length:   4.87 characters
Reading Time:      1.71 minutes
----------------------------------------
Top 5 Most Used Words:
  1. python       - 18 times
  2. code         - 12 times
  3. program      - 9 times
  4. data         - 7 times
  5. file         - 6 times
========================================

## ⚠️ Requirements
- Python 3.x
- No external libraries needed (`collections` is built-in)


---

**Quick tip:** The README is your project's front door — keep it clear and friendly. Anyone reading it should know *what* the project does and *how to run it* within 30 seconds. You're doing great! 🚀