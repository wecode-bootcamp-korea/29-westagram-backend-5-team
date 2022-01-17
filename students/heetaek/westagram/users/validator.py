import re

REGEX_EMAIL    = '^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
REGEX_PASSWORD = '^(?=.*[a-zA-Z])(?=.*[!@#$%^*+=-])(?=.*[0-9]).{8,}$'

def is_password(password):
    if not re.match(REGEX_PASSWORD, password):
        return False

def is_email(email):
    if not re.match(REGEX_EMAIL, email):
        return False