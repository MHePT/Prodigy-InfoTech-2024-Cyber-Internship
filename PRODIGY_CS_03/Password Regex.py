import re

def check_password_strength(password):
    strength = 0
    feedback = []

    if len(password) >= 12:
        strength += 1
    else:
        feedback.append("Password is too short. Minimum length should be 12 characters.")

    if re.search(r'[a-z]', password):
        strength += 1
    else:
        feedback.append("Password should include at least one lowercase letter.")

    if re.search(r'[A-Z]', password):
        strength += 1
    else:
        feedback.append("Password should include at least one uppercase letter.")

    if re.search(r'[0-9]', password):
        strength += 1
    else:
        feedback.append("Password should include at least one digit.")

    if re.search(r'[!@#$%^&*(),.?"\'\\:{}=|<>]', password):
        strength += 1
    else:
        feedback.append("Password should include at least one special character (e.g., !, @, #, $, etc.).")

    if strength == 5:
        return "Strong", feedback
    elif strength >= 3:
        return "Moderate", feedback
    else:
        return "Weak", feedback


if __name__ == "__main__":
    print("Password Strength Checker")
    password = input("Enter your password: ")
    
    strength, feedback = check_password_strength(password)
    
    print(f"Password Strength: {strength}")
    
    if feedback:
        print("Suggestions for improvement:")
        for tip in feedback:
            print(f"- {tip}")
