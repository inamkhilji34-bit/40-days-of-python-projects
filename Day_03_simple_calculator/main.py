# Simple Calculator for addition, Subtraction, Division, Product and Modulus.

# Operation Functions
def add(a,b):
    return a+b
def sub (a,b):
    return a-b
def product(a,b):
    return a*b
def division(a,b):
    if b == 0:
        print("Division by zero is not possible")
        return None
    return a/b
             
def modulus(a,b):
    if b == 0:
        print("Division by zero is not possible")
        return None
    return a % b
# Menu
while True:
    print("Please select one of the following operation you would like to perform")
    try:
        operations = int(input(" 1.Addition \n 2.Subtraction \n 3.Multiplication \n 4.Division \n 5.Modulus \n"))
    except ValueError:
        print("Enter the number instead of operation name.")
        continue

    # Invalid operation
    if operations not in range(1,6):
        print("Invalid choice. Choose between 1-5")
        continue
    # User input data
    try:
        x = float(input("Enter the first value:\t"))
        y = float(input("Enter the second value:\t"))
    except ValueError:
        print("Enter a valid number")
        continue
    
    match operations:
        case 1:
            print(f"{x} + {y} = {add(a=x, b=y)}")
        case 2:
            print(f"{x} - {y} = {sub(a=x, b=y)}")
        case 3:
            print(f"{x} * {y} = {product(a=x, b=y)}")
        case 4:
            result = division(a=x, b=y)
            if result is not  None:
                print(f"{x} / {y} = {result}")
        case 5:
            result = modulus(x,y)
            if result is not None: 
                print(f" {x} % {y} = {modulus(a=x, b=y)}")
    
    calc = input("Would you like to continue calculation (yes/no)? \n ").strip().lower()
    if calc == 'no':
        print("Thank you for using this calculator")
        break
