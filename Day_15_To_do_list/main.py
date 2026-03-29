import os

def load_tasks():
    try:
        with open('todo.txt', 'r') as file:
            tasks = file.readlines()
            return[task.strip() for task in tasks]
    except FileNotFoundError:
        return []
def save_tasks(tasks):
    with open('todo.txt', 'w') as file:
        for task in tasks:
            file.write(task + "\n")
def show_tasks(tasks):
    if not tasks:
        print("No tasks exist")
    else:
        print("Your to Do-List: ")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
        

tasks = load_tasks()
while True:
    print("--- To Do List---")
    print("1. View Task.")
    print("2. Add Task.")
    print("3. Delete a task.")
    print("4. Quit.")
    try:
        choice = int(input("Choose an option: "))
    except ValueError:
        print("Invalid input.")
        continue
    match choice:
        case 1:
            show_tasks(tasks)
        case 2:
            task = input("Enter the task: ")
            tasks.append(task)
            save_tasks(tasks)
            print("Task added.")
        case 3:
            show_tasks(tasks)
            try:
                num = int(input("Enter task number to remove: "))
                if 1 <= num <= len(tasks):
                    removed = tasks.pop(num - 1)
                    save_tasks(tasks)
                    print(f"✓ Removed: {removed}")
                else:
                    print("Invalid task number!")
            except ValueError:
                print("Please enter a number!")
        case 4:
            print("Good Bye.")
            break
    


