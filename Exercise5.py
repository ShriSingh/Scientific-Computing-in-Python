# Learning Regular Expressions by Building a Password Generator

import re
import secrets # --> For more natural(less predictive) random number generation
import string


def generate_password(length=16, nums=1, special_chars=1, uppercase=1, lowercase=1):
    """
    Generate a random password of a given length and certain constraints
    : param length: The length of the password
    : param nums: The minimum number of digits
    : param special_chars: The minimum number of special characters
    : param uppercase: The minimum number of uppercase letters
    : param lowercase: The minimum number of lowercase letters
    : return: The generated password
    """
    # Define the possible characters for the password
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    # Combine all characters
    all_characters = letters + digits + symbols

    while True:
        password = ''
        # Generate password
        for _ in range(length): # Using _ to use for loop without using the variable
            password += secrets.choice(all_characters)
        
        constraints = [ # r -> raw string (to avoid escape characters)
            (nums, r'\d'), # Same as r'[0-9]'
            (special_chars, fr'[{symbols}]'), # Same as r'[^a-zA-Z0-9]'
            (uppercase, r'[A-Z]'), # All uppercase letters
            (lowercase, r'[a-z]') # All lowercase letters
        ]

        # Check constraints using list comprehension       
        if all( # Returns True if all constraints are met
            constraint <= len(re.findall(pattern, password)) # Checks if any of the constraints are found in the password
            for constraint, pattern in constraints # Through all types of constraints
        ):
            break
    
    return password

if __name__ == '__main__':
    new_password = generate_password()
    print('Generated password:', new_password)