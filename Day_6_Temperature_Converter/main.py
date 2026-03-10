
def celsius_1(c2f):
    f = (c2f * 9/5) + 32
    print(f"Temperature in Fahrenheit is: {f}")

def celsius_2(f2c):
    c = (f2c - 32) * 5/9
    print(f"Temperature in Celsius is: {c}")

def kelvin_1(c2k):
    k = c2k + 273.15
    print(f"Temperature in kelvin is: {k}")

def kelvin_2(k2c):
    c2 = k2c - 273.15
    print(f'Temperature in Celsius is: {c2}')

def faren_1(f2k):
    f1 = (f2k - 32) * 5/9 + 273.15
    print(f"Temperature in kelvin: {f1}")

def faren_2(k2f):
    k2 = (k2f - 273.15) * 9/5 + 32
    print(f"Temperature in Fahrenheit is: {k2}")
    
def temperature():
    while True:
        try:
            menu= int(input("Welcome to temperature converter.\nWhat conversion do you want to perform?.\n1.Celsius to Fahrenheit \n2.Fahrenheit to Celsius \n3.Celsius to Kelvin \n4.Kelvin to Celsius \n5.Fahrenheit to Kelvin \n6.Kelvin to Fahrenheit \n"))
        except ValueError:
            print("Please enter a valid number")
            continue

        if menu not in range(1,7):
            print("Please, Choose between 1 to 6.")
            continue 
        
        try: 
            match menu:
                case 1:
                    c2f = float(input("Enter the temperature value: "))
                    return celsius_1(c2f)
                case 2:
                    f2c = float(input("Enter the temperature value: "))
                    return celsius_2(f2c)
                case 3:
                    c2k = float(input("Enter the temperature value: "))
                    return kelvin_1(c2k)
                case 4:
                    k2c = float(input("Enter the temperature value: "))
                    if k2c < 0:
                        print("Please enter valid kelvin value.")
                        return None
                    return kelvin_2(k2c)
                case 5:
                    f2k = float(input("Enter the temperature value: "))
                    return faren_1(f2k)
                case 6:
                    k2f = float(input("Enter the temperature value: "))
                    if k2f < 0:
                        print("Please, Enter a valid Kelvin temperature")
                        return None
                    return faren_2(k2f)
        except ValueError:
            print("Please enter a valid temperature value")
            

    
temperature()
while True:
    again = input("Try another?. (Yes/No).\n").strip().lower()
    if again == 'no':
        print("Thank you")
        break
    elif again == 'yes':
        temperature()
    else:
        print("Please, Enter 'Yes' or 'No'.")
        