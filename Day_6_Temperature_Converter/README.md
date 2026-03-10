# 🌡️ Day 6: Temperature Converter

Welcome to Day 6 of your Python journey! Today you're building a **Temperature Converter** that can convert between Celsius, Fahrenheit, and Kelvin.

## 📋 Project Overview

**Difficulty:** Easy  
**Concepts Covered:** Functions, dictionaries, menu systems, user input validation

## 🎯 What You'll Build

A program that displays a menu with 6 conversion options:
1. Celsius → Fahrenheit
2. Celsius → Kelvin
3. Fahrenheit → Celsius
4. Fahrenheit → Kelvin
5. Kelvin → Celsius
6. Kelvin → Fahrenheit

## 🔑 Key Formulas

You'll need these conversion formulas:

# From Celsius
F = C * 9/5 + 32
K = C + 273.15

# From Fahrenheit
C = (F - 32) * 5/9
K = (F - 32) * 5/9 + 273.15

# From Kelvin
C = K - 273.15
F = (K - 273.15) * 9/5 + 32


## 🛠️ Requirements

Your program should:
- [ ] Display a clear menu with all 6 conversion options
- [ ] Get the temperature value from the user
- [ ] Perform the correct conversion based on user choice
- [ ] Display the result with proper formatting
- [ ] Use functions for each conversion pair
- [ ] Use a dictionary to map menu choices to functions
- [ ] Handle invalid input gracefully

## 💡 Helpful Hints

1. **Create separate functions** for each conversion (6 total)
2. **Use a dictionary** to map numbers (1-6) to function names
3. **Round results** to 2 decimal places for cleaner output
4. **Add a loop** so users can do multiple conversions without restarting

## 📝 Example Output

=== Temperature Converter ===
1. Celsius → Fahrenheit
2. Celsius → Kelvin
3. Fahrenheit → Celsius
4. Fahrenheit → Kelvin
5. Kelvin → Celsius
6. Kelvin → Fahrenheit
7. Exit

Choose an option (1-7): 1
Enter temperature in Celsius: 25
25.0°C = 77.0°F

Choose an option (1-7): 5
Enter temperature in Kelvin: 300
300.0K = 26.85°C


## 🚀 Getting Started

Start by creating your conversion functions:

def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

# ... create the other 4 functions


Then create a dictionary to map choices:

conversions = {
    1: celsius_to_fahrenheit,
    2: celsius_to_kelvin,
    # ... add the rest
}


## 🎓 Learning Goals

By completing this project, you'll practice:
- Writing reusable functions
- Using dictionaries for mapping
- Creating menu-driven programs
- Handling user input
- Formatting output

## 🌟 Bonus Challenges

Once you've got the basic version working, try these:
- Add input validation (no negative Kelvin values!)
- Show conversions in all 3 units at once
- Add more temperature scales (Rankine, Réaumur)
- Save conversion history

---

**Remember:** Programming is about problem-solving step by step. Start simple, test often, and build up! You've got this! 💪