def table():
    while True:
            try:
                n = int(input("Enter the number for multiplication table:\n"))
                if n <= 0:
                     print("Enter a positive number")
                     continue
                for i in range(1,11):
                    print(f"{n} * {i} = {n*i}")
                break
            except ValueError:
                print("Please enter a valid number")
            continue
table()

while True:
    tb_1 = input("Would you like to find another table (Yes/No)? \n").lower()
    if tb_1 == 'no':
        print("Thank You")
        break 
    elif tb_1 == 'yes':
         table()
    else:
         print("Please enter 'yes' or 'no'")
     


    