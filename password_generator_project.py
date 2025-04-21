import random
import string

def generate_password(length=12):
    # Define character sets
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    # Combine all characters
    all_chars = letters + digits + symbols

    # Generate password
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

# Ask user for password length
try:
    user_length = int(input("🔐 Enter desired password length: "))
    password = generate_password(user_length)
    print(f"✅ Your secure password: {password}")
except ValueError:
    print("❌ Please enter a valid number.")
