from hashlib import sha512
from hmac import new
from os import urandom, getenv


def generate_hmac(identifier: str) -> tuple[str, str]:
    salt = urandom(32)
    secret_key = getenv("SECRET_KEY").encode()
    h = new(secret_key, salt + identifier.encode(), sha512)
    return h.hexdigest(), salt.hex()
