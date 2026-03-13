print("Starting Fizz-Buzz...")
while True:
    num_1 = int(input("Enter first number: "))
    word_1 = input("Enter first word: ")
    num_2 = int(input("Enter second number: "))
    word_2 = input("Enter second word: ")

    if num_1 <= 0 or num_2 <= 0:
        print("Number must be positive and greater than zero")
        continue
    elif num_1 == num_2:
        print("Enter different numbers to make game more interesting.")
        continue
    break

for i in range(1,51):
    if i % num_1 == 0 and i % num_2 == 0:
        print(word_1+'-'+word_2)
    elif i % num_1 == 0:
        print(word_1)
    elif i % num_2 == 0:
        print(word_2)
    else:
        print(i)