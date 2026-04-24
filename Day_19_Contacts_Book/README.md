# Contact Book - README 📒

Here's a clean README file for your project:

# 📒 Contact Book

A simple command-line Contact Book application built with Python.
Store, search, and manage your contacts — all saved to a JSON file!

---

## 📁 Project Structure

contact_book/
│
├── contact_book.py   # Main application file
└── contacts.json     # Auto-created when you add your first contact

---

## 🚀 Features

- ✅ Add a new contact (name, phone, email)
- 🔍 Search for a contact by name
- 🗑️ Delete a contact
- 📋 List all contacts
- 💾 Data saved automatically to a JSON file

---

## 🛠️ Requirements

- Python 3.x
- No external libraries needed (uses built-in `json` module)

---

## ▶️ How to Run

bash
python contact_book.py

---

## 💡 How to Use

When you run the program, you'll see a menu like this:


===== Contact Book =====
1. Add Contact
2. Search Contact
3. Delete Contact
4. List All Contacts
5. Quit

Just enter the number of the action you want!

---

## 📄 Example Contact (stored in JSON)

json
[
  {
    "name": "Alice Smith",
    "phone": "555-1234",
    "email": "alice@example.com"
  }
]

---

## 🧠 Concepts Practiced

- Reading and writing JSON files (`json.load`, `json.dump`)
- Functions and modular code
- List operations
- Using `next()` with a generator for searching
- Command-line menu with a loop

---

## 👨‍💻 Author

Made as part of a **30 Days of Python** challenge — Day 19!


---

You're doing great making it to Day 19! Want me to help you build the actual `contact_book.py` code next? 😊