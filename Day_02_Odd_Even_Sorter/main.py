print("Welcome to Number Sorting Game")

def number_sorter():
    odd_numbers = []
    even_numbers = []
    print("Enter a list of numbers and I will sort them into odd and even.")
    while True:
        try:
            n = int(input("Enter how many number you want to sort? \t"))
            break
        except ValueError:
            print("Enter a valid number")

    for i in range(n):
        while True:
            try:
                num = int(input(f"Enter number {i+1}: "))
                break
            except ValueError:
                print("Enter a valid number")
                continue
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            odd_numbers.append(num)
    print(f"Evens: {even_numbers}")
    print(f"Odds: {odd_numbers}")

while True:
    choice = input("Please Enter Yes to continue or 'quit' to exit \t")
    if choice == 'quit':
        print("Thank you for participating")
        break
    number_sorter()