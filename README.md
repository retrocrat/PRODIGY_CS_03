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
