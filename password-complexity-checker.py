import re

def evaluate_password_strength(password):
    # Define password criteria
    has_min_length = len(password) >= 8
    has_uppercase = re.search(r'[A-Z]', password)
    has_lowercase = re.search(r'[a-z]', password)
    has_digit = re.search(r'[0-9]', password)
    has_special_char = re.search(r'[\W_]', password)

    # Count criteria met 
    criteria_met = sum([
        has_min_length,
        bool(has_uppercase),
        bool(has_lowercase),
        bool(has_digit),
        bool(has_special_char)
    ])

    # Determine password strength
    if criteria_met == 5:
        strength = "Strong"
    elif criteria_met >= 3:
        strength = "Moderate"
    else:
        strength = "Weak"
    
    # Generate feedback
    feedback = []
    if not has_min_length:
        feedback.append("Password should be at least 8 characters long.")
    if not has_uppercase:
        feedback.append("Password should include at least one uppercase letter.")
    if not has_lowercase:
        feedback.append("Password should include at least one lowercase letter.")
    if not has_digit:
        feedback.append("Password should include at least one number.")
    if not has_special_char:
        feedback.append("Password should include at least one special character.")

    return strength, feedback

# Main program #https://github.com/retrocrat/PRODIGY_CS_03/password-complexity-checker.py
if __name__ == "__main__":
    password = input("Enter a password to evaluate its strength: ")
    strength, feedback = evaluate_password_strength(password)

    print(f"Password Strength: {strength}")
    if feedback:
        print("Feedback:")
        for suggestion in feedback:
            print(f"- {suggestion}")
    else:
        print("Your password is strong and meets all criteria!")
