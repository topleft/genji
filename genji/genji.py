import uuid
import string
import random

def gen_uuid():
    return uuid.uuid4()

def gen_password(length=10):
    character_sets = [
        string.ascii_letters,
        string.digits,
        string.punctuation,
    ]
    password = ''
    for i in range(length):
        password += random.choice(random.choice(character_sets))

    return password

