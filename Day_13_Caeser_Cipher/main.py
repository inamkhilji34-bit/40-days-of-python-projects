msg = input("Enter a message: ")
try:
    shift =int(input("Enter a shift (1-25): ") )
    if not (1<= shift <= 25):
         print('Please Enter a valid shift(1-25)')
         exit()
except ValueError:
     print("Enter a valid shift(1-25).")
     exit()
code = input("Type 'Encode' to encrypt or 'Decode' to decrypt: ").lower()

if code not in ["encode", "decode"]:
     print("Please enter a valid value.")
else:
    def caesar(msg,shift,code):
        result = ''
        
        if code == 'decode':
                shift = - shift

        for char in msg:
            if char.isalpha():
                ascii_val  = ord(char)
            
                if char.isupper():
                    shifted = ((ascii_val - 65 + shift) % 26) + 65
                else:
                    shifted = ((ascii_val - 97 + shift) % 26) + 97
                result += chr(shifted)
            else:
                result += char
        return result

output = caesar(msg,shift, code)
print(f"The {code} of text is {output}: ")


