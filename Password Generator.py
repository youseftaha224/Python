import random
import string

def generate_password(length = 12):

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    all = lowercase + uppercase + digits + special_characters

    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special_characters)
    ]

    for _ in range(length - 4):
        password.append(random.choice(all))

    random.shuffle(password)
    return "".join(password)

try:
    length = int(input("Enter password's length: "))
    if length < 4:
        print("Password length too short. Using default length of 12.")
        length = 12
except ValueError:
    print("Invalid input. Using default length of 12.")
    length = 12

password = generate_password(length)
print(f"Generated Password: {password}")