import re

def assess_password_strength(password):
    # Define the criteria
    criteria = {
        "length": len(password) >= 8,
        "uppercase": bool(re.search(r'[A-Z]', password)),
        "lowercase": bool(re.search(r'[a-z]', password)),
        "digit": bool(re.search(r'\d', password)),
        "special_char": bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
    }
    
    # Evaluate the password strength
    score = sum(criteria.values())
    
    # Provide feedback based on the score
    if score == 5:
        strength = "Strong"
        feedback = "Your password is strong!"
    elif score == 4:
        strength = "Moderate"
        feedback = "Your password is good, but consider adding more complexity."
    elif score == 3:
        strength = "Weak"
        feedback = "Your password is weak. Consider making it longer and adding a mix of uppercase letters, numbers, and special characters."
    else:
        strength = "Very Weak"
        feedback = "Your password is very weak. It needs significant improvement, including length and complexity."
    
    # Detailed feedback on missing criteria
    if not criteria["length"]:
        feedback += " Make sure your password is at least 8 characters long."
    if not criteria["uppercase"]:
        feedback += " Add uppercase letters."
    if not criteria["lowercase"]:
        feedback += " Add lowercase letters."
    if not criteria["digit"]:
        feedback += " Add numbers."
    if not criteria["special_char"]:
        feedback += " Add special characters."

    return strength, feedback

# Example usage:
password = input("Enter your password: ")
strength, feedback = assess_password_strength(password)
print(f"Password Strength: {strength}")
print(f"Feedback: {feedback}")
