# Day 15: Todo List + File Save 📝

A simple command-line todo list application that saves your tasks to a file, so they persist between sessions!

## 🎯 What You'll Learn
- Reading and writing files in Python
- Using `open()`, `writelines()`, and `readlines()`
- Building a practical CLI application
- Data persistence basics

## ✨ Features
- Add new tasks
- View all tasks
- Mark tasks as complete
- Delete tasks
- **Save tasks to `todos.txt`**
- **Auto-load tasks when program starts**

## 🚀 Getting Started

### Basic File Operations
# Save tasks to file
with open('todos.txt', 'w') as file:
    file.writelines(tasks)

# Load tasks from file
with open('todos.txt', 'r') as file:
    tasks = file.readlines()


## 💡 Implementation Tips

1. **Load on startup**: Read from file when program starts
2. **Save after changes**: Write to file after adding/deleting tasks
3. **Handle missing file**: Use try/except if file doesn't exist yet
4. **Strip newlines**: Use `.strip()` when reading tasks

## 📋 Example Output
=== Todo List ===
1. [ ] Buy groceries
2. [ ] Learn Python
3. [✓] Complete Day 15

Options:
1. Add task
2. Complete task
3. Delete task
4. Exit


## 🎓 Challenge Yourself
- Add task priorities (high/medium/low)
- Use JSON instead of .txt for better data structure
- Add due dates to tasks
- Create separate files for completed tasks

Happy coding! 🐍✨