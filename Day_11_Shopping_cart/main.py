cart = {
    "apple": {"price": 3, "qty": 7},
    "soap" : {"price": 2, "qty": 2},
    "milk" : {"price": 5, "qty": 3},
    "rice" : {"price": 9, "qty": 1}
}
while True:
    try:
        menu = int(input("1.Add item\n2.Remove item\n3.view Cart\n4.Update Quantity\n5.Clear Cart\n6.Quit\n"))
    except ValueError:
        print("Enter a valid number(1-6)")
        continue

    match menu:
        case 1:
            
            item_name = input("Enter item name: ").lower()
            try:
                item_qty = int(input("Enter item quantity: "))
            except ValueError:
                print("Please enter valid value.")
                continue
            if item_name in cart:
                cart[item_name]["qty"] += item_qty
                print(f"{item_name} updated.")
            else:
                price = float(input("Enter price: "))
                cart[item_name] = {"price":price, "qty": item_qty }
                print(f"{item_name} added.")
        case 2:
            item_name = input("Enter item name: ").lower()
            if item_name in cart:
                cart.pop(item_name)
                print(f"{item_name} removed.")
            else:
                print(f"{item_name} does not exist.")
        case 3:
            if not cart:
                print("Your cart is empty.")
            else:
                print(f"\n{'Item':<15} {'price':>8} {'qty':>6} {'Subtotal':>10}")
                print("-" * 42)
                total = 0
                for key, value in cart.items():
                    subtotal = value["price"] * value["qty"]
                    total += subtotal
                    print(f"{key:<15} £{value['price']:>7.2f} {value['qty']:>6} £{subtotal:>9.2f}")
                print("-" * 42)
                print(f"{'Grand Total':<15} {'':>15} £{total:>9.2f}")
        case 4:
            item_name = input("Enter item name: ").lower()
            try:
                item_qty = int(input("Enter item quantity: "))
            except ValueError:
                print("Enter a valid value.")
                continue
            if item_name not in cart:
                print("Item does not exist in the cart. Add it")
            else:
                cart[item_name]["qty"] += item_qty
                print(f"{item_name} updated.")
        case 5:
            cart.clear()
            print("Your cart has been cleared.")
        case 6:
            exit()


        


            
