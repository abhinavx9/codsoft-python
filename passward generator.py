#Simple Password Generator
import random
import string

def generate_password(length=8):
    # Defining character pool
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a random password
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password
password_length = 8
generated_password = generate_password(password_length)

print("Generated Password:", generated_password)
