import random
import string

def generate_password(length=12):
    # Define the characters to use in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password by selecting 'length' characters from the defined set
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

# Ask the user for the desired password length
try:
    length = int(input("Enter the desired password length: "))
    if length < 1:
        print("Password length must be greater than 0.")
    else:
        password = generate_password(length)
        print("Generated Password:", password)
except ValueError:
    print("Please enter a valid number for password length.")
