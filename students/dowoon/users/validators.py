import re

from users.models import User


def validate_email(email):
    email_pattern = re.compile("^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
    bool_email_pattern_result = bool(email_pattern.match(email))
    return bool_email_pattern_result

def validate_password(password):
    password_pattern = re.compile("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$@$!%*?&])[A-Za-z\d$@$!%*?&]{8,}")
    bool_password_pattern_result = bool(password_pattern.match(password))
    return bool_password_pattern_result

def validate_duplicate(email):
    try:
        user = User.objects.get(email=email)
        if user.email == email:
            return True
    except User.DoesNotExist:
        return False
