# Caesar Cipher - Day 13 Project

A Python implementation of the classic Caesar Cipher encryption and decryption tool.

## 📋 Description

The Caesar Cipher is one of the oldest and simplest encryption techniques. This program allows you to:
- **Encode** messages by shifting letters forward in the alphabet
- **Decode** messages by shifting letters backward
- Choose any shift value from 1-25
- Preserve spaces, punctuation, and formatting

## ✨ Features

- ✅ Encode and decode messages
- ✅ User-selected shift amount (1-25)
- ✅ Handles both uppercase and lowercase letters
- ✅ Preserves spaces and punctuation
- ✅ Wraps around the alphabet automatically

## 🚀 How to Use

1. Run the program:
python caesar_cipher.py


2. Follow the prompts:
   - Enter your message
   - Choose a shift number (1-25)
   - Type 'encode' to encrypt or 'decode' to decrypt

## 💡 Example

Type your message: Hello, World!
Type the shift number (1-25): 5
Type 'encode' to encrypt or 'decode' to decrypt: encode

The encoded text is: Mjqqt, Btwqi!


To decode:
Type your message: Mjqqt, Btwqi!
Type the shift number (1-25): 5
Type 'encode' to encrypt or 'decode' to decrypt: decode

The decoded text is: Hello, World!


## 🔧 How It Works

The program uses:
- `ord()` - Converts characters to ASCII values
- `chr()` - Converts ASCII values back to characters
- Modulo 26 (`% 26`) - Wraps around the alphabet
- Separate handling for uppercase (A-Z) and lowercase (a-z)

### The Math Behind It

For lowercase letters:
shifted = ((ascii_value - 97 + shift) % 26) + 97


- Subtract 97: Convert to 0-25 range (a=0, b=1, etc.)
- Add shift: Move forward in alphabet
- Mod 26: Wrap around if needed
- Add 97: Convert back to ASCII

## 📚 Learning Objectives

- String manipulation
- ASCII character encoding
- User input handling
- Functions and conditional logic
- Modular arithmetic

## 🎯 Skills Practiced

- Working with `ord()` and `chr()` functions
- Character type checking with `.isalpha()`, `.isupper()`
- Building reusable functions
- Input validation

## 🔮 Future Enhancements

- Add brute force decoder (tries all 25 shifts)
- Save encrypted messages to files
- GUI interface
- Support for other languages/alphabets

---

**Difficulty:** Medium  
**Day:** 13  
**Language:** Python 3.x

Happy encrypting! 🔐