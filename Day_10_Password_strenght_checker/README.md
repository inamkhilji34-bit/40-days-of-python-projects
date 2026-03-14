# Day 10: Password Strength Checker 🔒

Welcome to Day 10 of your Python journey! Today, you'll build a **Password Strength Checker** that evaluates how secure a password is.

---

## 🎯 Your Mission

Create a program that scores a password from **0 to 5** based on security rules. The program should:
- Calculate a strength score
- Show which rules the password passes or fails
- Give helpful feedback to the user

---

## 📋 The 5 Rules

Your password checker should test for:

1. **Length**: At least 8 characters
2. **Uppercase**: Contains at least one uppercase letter (A-Z)
3. **Lowercase**: Contains at least one lowercase letter (a-z)
4. **Digit**: Contains at least one number (0-9)
5. **Special Character**: Contains at least one symbol (!@#$%^&*, etc.)

Each rule passed = +1 to the score!

---

## 💡 Key Hint

Use Python's `any()` function with generator expressions:

# Check if password has an uppercase letter
has_uppercase = any(c.isupper() for c in password)

# Check if password has a digit
has_digit = any(c.isdigit() for c in password)


---

## 📝 Example Output

Enter a password to check: hello

Password Strength: 1/5 (Weak)

❌ Must be at least 8 characters
❌ Must contain an uppercase letter
✓ Contains a lowercase letter
❌ Must contain a digit
❌ Must contain a special character


Enter a password to check: MyP@ssw0rd

Password Strength: 5/5 (Very Strong)

✓ At least 8 characters
✓ Contains an uppercase letter
✓ Contains a lowercase letter
✓ Contains a digit
✓ Contains a special character


---

## 🚀 Challenge Yourself

Once you've got the basic version working, try:
- Adding strength labels (Weak, Fair, Good, Strong, Very Strong)
- Colored output using emojis (🔴 🟡 🟢)
- Suggesting what the user needs to add
- Testing multiple passwords in a loop

---

## 🎓 What You'll Learn

- Using `any()` with generator expressions
- String methods: `.isupper()`, `.islower()`, `.isdigit()`
- Conditional logic and scoring systems
- User-friendly feedback

---

## ✨ Tips

- Start by checking one rule at a time
- Test with simple passwords first ("abc", "ABC123")
- Use variables to store each rule's result
- Print as you go to debug!

---

**Ready to start coding? You've got this! 💪**