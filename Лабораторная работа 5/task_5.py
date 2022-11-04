import string
import random


def get_random_password() -> str:
    b = string.ascii_uppercase + string.ascii_lowercase + string.digits
    password = random.sample(b, 8)
    return password


print(get_random_password())
