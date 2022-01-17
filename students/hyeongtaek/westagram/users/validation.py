import re

from django.validation import ValidationError

from users.models import User

def validate_email(email):
    if re.match("^[a-zA-Z0-9._+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9.]+$",email):
        raise validate_email({"message": "SUCCESS"})

def validate_password(password):
    if re.match("^[a-zA-Z0-9._+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9.]+$",password):
        raise validate_password({"message": "SUCCESS"})
    if len(password)<8:
        raise ValidationError({"ERROR": "비밀번호는 8자이상입력"})

def validate_email_duplicatecheck(email):
    if not re.match(email=data[email]):
        raise ValidationError({"ERROR": "중복된 이메일입니다"}) 






