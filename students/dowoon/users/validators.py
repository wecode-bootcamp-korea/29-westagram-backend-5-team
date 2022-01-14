import re

from users.models import User


def validate_email(email):
    if not re.match("^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email):
        raise Exception("ERROR : INVALID_VALUE (email)")

def validate_password(password):
    if not re.match("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$@$!%*?&])[A-Za-z\d$@$!%*?&]{8,}", password):
        raise Exception("ERROR : INVALID_VALUE (password)")

def validate_duplicate(email):
    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        if user.email == email:
            raise Exception("ERROR : DUPLICATE")

