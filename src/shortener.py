import string
from secrets import choice

ALPHABET = string.ascii_letters + string.digits


def generate_random_slug() -> str:
    slug = ""
    for i in range(6):
        char = choice(ALPHABET)
        slug += char
    return slug
