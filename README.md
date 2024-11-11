# Password Complexity Checker

This Python script is a **Password Complexity Checker** that evaluates the strength of user passwords by checking if they meet specific security criteria. The tool assesses the password's strength as **Strong**, **Moderate**, or **Weak** based on several conditions and provides feedback to help users create more secure passwords.

## Features:
  - **Password Strength Evaluation**: The tool categorizes the password strength into three levels:
  - **Strong**: Meets all five security criteria.
  - **Moderate**: Meets at least three criteria.
  - **Weak**: Meets fewer than three criteria.
- **Detailed Feedback**: If the password doesn’t meet one or more criteria, the tool provides clear suggestions for improvement, such as adding uppercase letters, numbers, or special characters.
- **User Input**: The program prompts the user to input a password and then evaluates it based on the defined strength criteria.

## Getting Started

- Clone the repository:

```git clone https://github.com/retrocrat/PRODIGY_CS_03.git```

- Run the script:

```python password-complexity-checker.py```

## How It Works:
1. **Criteria Checking**: The function `evaluate_password_strength` uses regular expressions (`re.search`) to check for the following criteria:
   - A minimum length of 8 characters.
   - At least one uppercase letter.
   - At least one lowercase letter.
   - At least one digit.
   - At least one special character (non-alphanumeric).
   
2. **Strength Evaluation**: It counts how many of these criteria the password meets and determines the strength:
   - If all 5 criteria are met, the password is deemed **Strong**.
   - If 3 or more criteria are met, it's considered **Moderate**.
   - Otherwise, it is **Weak**.
   
3. **Feedback Generation**: Based on which criteria the password fails to meet, the program generates feedback and suggests improvements. If the password meets all criteria, it congratulates the user.

## Technologies Used:
- **Python**: The script is written in Python, leveraging the standard library for string manipulation and regular expressions.
- **Regular Expressions (re module)**: Used to search for specific patterns in the password, such as uppercase letters, digits, and special characters.
- **Input/Output Handling**: The program uses `input()` to capture the user’s password and `print()` to display the results and feedback. 

This tool is an effective way to ensure password security by guiding users to create stronger, more secure passwords.

### Code

Here is the Python code for the Password Complexity Checker:

```
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

# Main program
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
