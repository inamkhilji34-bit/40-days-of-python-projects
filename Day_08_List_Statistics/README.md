# Day 8: List Statistics (Easy)

## 📋 Task Description
Create a program that asks the user for 5 numbers, then calculates and displays various statistics about those numbers.

## 🎯 Learning Objectives
- Working with lists in Python
- Using built-in functions: `sum()`, `min()`, `max()`
- Understanding list comprehensions
- Practicing user input and type conversion

## 📊 Required Statistics
Your program should display:
1. **Sum** - Total of all numbers
2. **Average** - Mean value
3. **Minimum** - Smallest number
4. **Maximum** - Largest number
5. **Range** - Difference between max and min
6. **Negative Check** - Whether any number is negative

## 💡 Key Hints
- Use `sum()` to add all numbers
- Use `min()` to find the smallest
- Use `max()` to find the largest
- Range = `max(nums) - min(nums)`
- Check for negatives: `any(x < 0 for x in nums)`

## 📝 Example Output
Enter number 1: 10
Enter number 2: -5
Enter number 3: 20
Enter number 4: 8
Enter number 5: 3

=== Statistics ===
Sum: 36
Average: 7.2
Minimum: -5
Maximum: 20
Range: 25
Contains negative numbers: Yes


## 🚀 Getting Started

# Create an empty list
numbers = []

# Get 5 numbers from the user
for i in range(1, 6):
    num = float(input(f"Enter number {i}: "))
    numbers.append(num)

# Now calculate your statistics!


## ✅ Checklist
- [ ] Create a list to store numbers
- [ ] Get 5 numbers from user input
- [ ] Calculate sum using `sum()`
- [ ] Calculate average (sum ÷ count)
- [ ] Find minimum using `min()`
- [ ] Find maximum using `max()`
- [ ] Calculate range (max - min)
- [ ] Check if any number is negative
- [ ] Display all results clearly

## 🎓 Bonus Challenges
- Format the average to 2 decimal places
- Add more statistics (median, count of positives)
- Allow the user to enter any number of values
- Handle non-numeric input gracefully

Happy coding! 🐍✨