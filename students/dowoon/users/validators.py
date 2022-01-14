import re

from django.core.exceptions import ValidationError

from users.models import User


def validate_email(email):
    email_match_result = re.match("^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email)
    if email_match_result == None:
        raise ValidationError(
            message = ('INVALID VALUE'),
            code    = 'invalid'
        )

def validate_password(password):
    password_match_result = re.match("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$@$!%*?&])[A-Za-z\d$@$!%*?&]{8,}", password)
    if password_match_result == None:
        raise ValidationError(
            message = ('INVALID VALUE'),
            code    = 'invalid',
        )

def validate_duplicate(email):
    user = User.objects.get(email=email)
    if user.email == email:
        raise ValidationError(
            message = ('DUPLICATE'),
            code    = 'invalid',
        )

