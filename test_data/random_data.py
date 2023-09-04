import secrets
import string

digits_for_double_number = '123456789'
def get_random_digits(password_len: int = 1) -> str:
    return "".join(secrets.choice(string.digits) for _ in range(password_len))

def get_double_random_digits(password_len: int = 2) -> str:
    return "".join(secrets.choice(digits_for_double_number) for _ in range(password_len))

def get_random_string(password_len: int = 5) -> str:
    return "".join(secrets.choice(string.ascii_lowercase) for _ in range(password_len))

def get_random_string_for_payload() -> str:
    return "".join(secrets.choice(string.ascii_lowercase) for _ in range(3, 10))

def get_random_email(email_len: int = 8) -> str:
    return "".join(secrets.choice(string.ascii_lowercase) for _ in range(email_len)) + "@mail.ru"