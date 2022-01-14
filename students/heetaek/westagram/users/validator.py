import re

def is_password(password):
    # 8자리 이상, 문자, 숫자, 특수문자의 비밀번호 유효성 검사
    password_regex = re.compile('^(?=.*[a-zA-Z])(?=.*[!@#$%^*+=-])(?=.*[0-9]).{8,}$')
    if not password_regex.match(password):
        return False

def is_email(email):
    # 이메일 유효성 검사
    email_regex = re.compile('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
    if not email_regex.match(email):
        return False