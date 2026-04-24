import json
import os

# Get the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(script_dir, "contacts.json")

# Load existing contacts if file exists
if os.path.exists(filename):
    with open(filename, 'r') as f:
        contacts = json.load(f)
else:
    contacts = {}
def save_contacts():
    with open(filename, 'w') as f:
            json.dump(contacts, f, indent=4)
            

while True:
    menu = int(input("Enter the number for each option:\n1.Add a contact \n2.Search \n3.Delete \n4.List \n5.Quit \n "))
    match menu:
        case 1:
            name = input("Enter your name: ")
            email = input("Enter your gmail: ")
            phone = input("Enter your phone number: ")

            contacts[name] = {
                "Gmail": email,
                "Phone_Number": phone
            }
            # Save contacts
            save_contacts()
            print("Contact added successfully.")
        case 2:
            user = input("Enter the user name: ")
            if user in contacts:
                print(contacts[user])
            else:
                print("User does not exist in contact book.")
        case 3:
            user_name = input("Enter name of user: ")
            if user_name in contacts:
                del contacts[user_name]
                # Save contacts after deletion
                save_contacts()
                print("User deleted Successfully.")
            else:
                print("User does not exist in the contact book.")
        case 4:
            for name,info in contacts.items():
                print(f"Name: {name} , \n Info: {info}")
        case 5:
            print("Goodbye!")
            break



