import random

print("welcome to Number Guessing Game!")

def number_guesser(name):
    number = random.randint(1,100)
    attempts = 0

    while True:
        try :
            ask_question = int(input("Guess the number (1,100) \n "))
        except ValueError:
            print("Please enter a valid number")
        else:
            attempts += 1
            if ask_question > number:
                print("Try again, Too High. \n")
            elif ask_question < number :
                print("Try again, Too Low. \n")
            else:
                print(f"Well done, You have guessed it in {attempts}.")
                break
while True:
    name = input("Please Enter your name to continue. \n Enter 'quit' to exit the game. \n ")
    if name == 'quit':
        print("Thank you for playing this game.")
        break

    number_guesser(name)

    again = input("Play again.(Yes/quit):").strip().lower()
    if again == 'quit':
        print(f"Good job {name}")
        print("Thank you for playing goodbye.")
        break


