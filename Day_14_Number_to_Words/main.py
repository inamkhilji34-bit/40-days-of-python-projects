# Number to Words
def number_to_words(n):
    if n < 1 or n > 999:
        return "Number out of range."
    
    ones = {
        1: 'one', 2: 'two', 3: 'three', 4:'four', 5: 'five', 6:'six', 7:'seven', 8:'eight', 9:'nine', 10:'ten', 11:'eleven', 12:'twelve', 13: 'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen'
        }
    tens = {
        20:'twenty', 30:'thirty', 40:'forty', 50:'fifty', 60:'sixty', 70:'seventy', 80:'eighty', 90:'ninety'
            }
    words = ""
    # Hundred's Place
    if n >= 100:
        words += ones[n//100] + " hundred "
        n %= 100

    # Ten's Place
    if n >= 20:
        words += tens[(n//10) * 10]
        if n % 10 != 0:
            words += " " + ones[n % 10]
    elif n > 0:
        words += ones[n]
    return words.strip()

try:
    n= int(input("Enter a number (1-999): "))
    print(number_to_words(n))
except ValueError:
    print("Enter a valid number.")
    



