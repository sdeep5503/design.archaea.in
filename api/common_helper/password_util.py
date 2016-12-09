import re


class PasswordHelper:

    def __init__(self):
        pass

    @staticmethod
    def validate_password(password):
        # Check if contains at least one digit, one uppercase character and a lowercase character
        if not re.search(r'\d', password) or not re.search(r'[A-Z]', password) \
                or not re.search(r'[a-z]', password):
            return False
        return True
