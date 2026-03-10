
def reverser():
    # Sentence Reverser
    sent = input("Enter a sentence to reverse.\n")
    words = sent.split()
    reversed_sent = words[::-1]
    print(f"Reversed Sentence: {' '.join(reversed_sent)}")
    
    # Word Reverser
    reverse_words = [word[::-1] for word in words]
    print(f"Reversed Words: {' '.join(reverse_words)}")

reverser()
# Loop Program
while True:
    again = input("Try another(yes/no). ").lower()
    if again == 'no':
        print("Thank you")
        break
    elif again == 'yes':
        reverser()
    else:
        print("Please, Enter 'yes' or 'no'.")