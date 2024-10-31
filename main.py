import random
import string

# Functionality to encrypt password and hide password 
import hashlib
import getpass

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

def main():
    # Ask user for password length
    length = int(input("Enter password length: "))

    # Generates password and stores it into a var in memory
    password = generated_random_password(length)

    # Ask for purpose of password
    purpose = input("What is this password for? ")

    # Formats how the passwords will get stored in the txt file
    entry = f"Password :{password}, Purpose: {purpose}\n"

    # Adds the password to the password.txt file
    # with open(file_path, mode, encoding) as file: SYNTAX
    with open('password.txt', 'a') as file:
        file.write(entry)
    
    print("Password and purpose saved to passwords.txt.")

if __name__ == "__main__":
    main()
