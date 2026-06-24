import random
import string

def generate_password(length):
    # Combine letters, digits, and punctuation marks
    all_characters = string.ascii_letters + string.digits + string.punctuation
    # Select characters randomly based on the chosen length
    password = "".join(random.choice(all_characters) for _ in range(length))
    return password

def test_strength(password):
    length = len(password)
    has_letter = any(c.isalpha() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)
    
    if length >= 12 and has_letter and has_digit and has_special:
        return "Strong 💪"
    elif length >= 8 and has_letter and has_digit:
        return "Medium ⚠️"
    else:
        return "Weak ❌"

if __name__ == "__main__":
    print("=== Hermione Password Tool ===")
    print("1. Generate a new password")
    print("2. Test a custom password strength")
    print("3. Exit")
    print("-" * 30)
    
    while True:
        choice = input("Choose an option (1-3): ").strip()
        
        if choice == "1":
            try:
                user_length = int(input("Enter desired password length: "))
                if user_length < 4:
                    print("Please choose a length of 4 or more.")
                else:
                    new_password = generate_password(user_length)
                    print(f"Generated Password: {new_password}")
                    print(f"Strength Rating: {test_strength(new_password)}")
            except ValueError:
                print("Please enter a valid number for length.")
                
        elif choice == "2":
            custom_input = input("Enter your password to test: ")
            print(f"Strength Rating: {test_strength(custom_input)}")
            
        elif choice == "3":
            print("Shutting down Password Tool. Goodbye!")
            break
        else:
            print("Invalid option. Choose 1, 2, or 3.")
        print("-" * 30) 
