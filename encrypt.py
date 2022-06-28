import os
import sys
import subprocess
import importlib
from cryptography.fernet import Fernet


def encrypt(filename, key):
    """
    Given a filename (str) and key (bytes), it encrypts the file
    and writes it.

    """
    f = Fernet(key)
    with open(filename, "rb") as reader:
        unencrypted_data = reader.read()
    encrypted_data = f.encrypt(unencrypted_data)
    with open(f'{filename}.encrypted', "wb") as writer:
        writer.write(encrypted_data)


if __name__ == '__main__':
    crypto_key = sys.argv[1]
    file = sys.argv[2]
    encrypt(file, crypto_key)
