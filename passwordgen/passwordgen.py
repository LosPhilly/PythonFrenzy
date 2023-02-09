import random
import string

def generate_password(length, chars):
    return ''.join(random.choice(chars) for i in range(length))

chars = string.ascii_letters + string.digits + string.punctuation
length = int(input("Enter the desired length of the password: "))
password = generate_password(length, chars)
print("Your random password is:", password)
