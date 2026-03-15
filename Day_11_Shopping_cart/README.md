# Day 11: Shopping Cart CLI (Medium)

Welcome to Day 11! Today you'll build a simple shopping cart system that manages items, quantities, and prices.

## 🎯 Project Goal

Create a command-line shopping cart application where users can:
- Add items with prices
- Remove items
- Update quantities
- View a running subtotal

## 💡 Key Concept

Use a dictionary to store your cart:
cart = {
    "apple": {"price": 1.50, "qty": 3},
    "banana": {"price": 0.75, "qty": 5}
}


## ✨ Features to Implement

1. **Add Item**: Add new items or update existing ones
2. **Remove Item**: Delete items from cart
3. **Update Quantity**: Change the quantity of an item
4. **Show Cart**: Display all items with their details
5. **Calculate Subtotal**: Show the total cost

## 🚀 Getting Started

### Basic Structure

cart = {}

def add_item(name, price, qty):
    # Add your code here
    pass

def remove_item(name):
    # Add your code here
    pass

def update_quantity(name, qty):
    # Add your code here
    pass

def show_cart():
    # Add your code here
    pass

def calculate_subtotal():
    # Add your code here
    pass


## 📝 Example Usage

Welcome to Shopping Cart!
1. Add item
2. Remove item
3. Update quantity
4. Show cart
5. Calculate subtotal
6. Exit

Choice: 1
Enter item name: apple
Enter price: 1.50
Enter quantity: 3
✓ Added apple to cart!

Choice: 4
--- Shopping Cart ---
apple: $1.50 x 3 = $4.50
---------------------
Subtotal: $4.50


## 🧪 Test Cases

Try these scenarios:
- Add multiple items
- Update an item's quantity to 0
- Remove a non-existent item
- Calculate subtotal with empty cart

## 💪 Bonus Challenges

Once you have the basics working:
- Add input validation (price > 0, qty > 0)
- Implement a "clear cart" function
- Add a discount code feature
- Save cart to a file

## 🎓 Learning Points

By completing this project, you'll practice:
- Working with nested dictionaries
- Dictionary methods (`.get()`, `.pop()`, etc.)
- Basic CRUD operations
- Formatting numbers as currency

## 🆘 Need Help?

**Common issues:**
- KeyError? Use `.get()` or check if key exists first
- Wrong subtotal? Make sure to multiply price × quantity
- Can't update? Remember to access nested dict: `cart[name]["qty"]`

Good luck! Remember, every expert programmer started where you are now. You've got this! 🌟