import random
import string

def generate_password(length=12, use_upper=True, use_digits=True, use_special=True):
    """Generate a random password based on user preferences."""
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase if use_upper else ""
    digits = string.digits if use_digits else ""
    special = string.punctuation if use_special else ""

    all_chars = lower + upper + digits + special
    if not all_chars:
        return "Error: No character set selected!"

    password = "".join(random.choice(all_chars) for _ in range(length))
    return password

def main():
    print("🔐 Welcome to the Password Generator!")
    
    try:
        length = int(input("Enter password length (default 12): ") or 12)
        use_upper = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
        use_digits = input("Include numbers? (y/n): ").strip().lower() == 'y'
        use_special = input("Include special characters? (y/n): ").strip().lower() == 'y'

        password = generate_password(length, use_upper, use_digits, use_special)
        print(f"\n🎉 Your generated password: {password}")
    
    except ValueError:
        print("❌ Error: Please enter a valid number for password length.")

if __name__ == "__main__":
    main()
