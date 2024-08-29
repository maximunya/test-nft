import random
import string

from .models import Token


def generate_unique_hash():
    while True:
        unique_hash = ''.join(random.choices(string.ascii_letters + string.digits, k=20))
        if not Token.objects.filter(unique_hash=unique_hash).exists():
            return unique_hash