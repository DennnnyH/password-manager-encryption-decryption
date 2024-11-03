import random
import string
# Gives access to functions and vars that can allow interaction with operating system. Ex: creating, deleting files
import os

# Functionality to encrypt password and hide password 
import hashlib
import getpass

# Encryption
from cryptography.fernet import Fernet

def generated_random_password(length):
    # Concatenates all the ASCII values into one string
    passwordValues = string.ascii_letters
    passwordValues += string.digits
    passwordValues += string.punctuation

    generated_password = ''

    # Loops through the length and randomly generates a new character for each iteration which gets added to password
    for i in range(length):
        next_character = random.choice(passwordValues)
        generated_password += next_character

    return generated_password

def display_entry():
    # Checks operating system to see if the file exists
    if os.path.exists("password.txt"):
        # Opens the txt file with intentions to read ('r')
        with open ('password.txt','r') as file:
            entries = file.readlines()
            print("\nCurrent Password Entries: ")
            # Keeps track of how many passwords have been generated 
            # strip() method removes any leading, and trailing whitespaces
            for i, entry in enumerate(entries):
                print(f"{i + 1}) {entry.strip()}")
    else:
        # Txt file does not exist (or path is wrong)
        print("No entries")


def delete_entry(entry_number):
    if os.path.exists("password.txt"):
        with open('password.txt','r') as file:
            entries = file.readlines()
        # Checks if the entry that wants to be deleted is between the beginning and end
        if 1 <= entry_number <= len(entries):
            # Removes the specific entry
            del entries[entry_number - 1]
            # Open txt file with intention to write ('w')
            with open('password.txt','w'):
                # Writes the remaining entries back
                file.writelines(entries)
            print("Entry deleted")
        else:
            print("Invalid entry number")
    else:
        print("No entry found")

def generate_key():
    key = Fernet.generate_key()
    return key
    print(key)

def main():
    while True:
        key = Fernet.generate_key()
        print(key)
        print(key)
        print(key)

        print("\nMenu:")
        print("1. Generate new password")
        print("2. Display current password entries")
        print("3. Delete a password entry")
        print("4. Exit")

        choice = (input("Choose an option: "))

        if choice == '1':
            # Ask user for password length
            length = int(input("Enter password length: "))

            # Generates password and stores it into a var in memory
            password = generated_random_password(length)

            # Ask for purpose of password
            purpose = input("What is this password for? ")

            # Formats how the passwords will get stored in the txt file
            entry = f"Password : {password} || Purpose: {purpose}\n"

            # Adds the password to the password.txt file
            # with open(file_path, mode, encoding) as file: SYNTAX
            with open('password.txt', 'a') as file:
                file.write(entry)
    
            print("Password and purpose saved to passwords.txt.")

        elif choice == '2':
            display_entry()

        elif choice == '3':
            display_entry()
            entry_number = int(input("Enter entry you want to delete: "))
            delete_entry(entry_number)

        elif choice == '4':
            break

        else:
            print("Invalid number! Try again")

if __name__ == "__main__":
    main()
