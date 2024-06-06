import random
import string

def generate_password(length=6):
    all_characters = string.ascii_letters + string.digits + '!@#$%^&*()_+=-'

    password = ''.join(random.choices(all_characters, k=length))

    return password

user_input = input("Enter the password length (default 6): ")
length = int(user_input) if user_input else 6

password = generate_password(length)
print("The password is:", password)
