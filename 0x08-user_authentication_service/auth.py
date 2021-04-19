#!/usr/bin/env python3
"""
    hash password
"""
from bcrypt import hashpw, gensalt, checkpw


def _hash_password(password: str) -> str:
    """
        Returned bytes is a salted hash of the input password
    """
    return hashpw(password.encode('utf-8'), gensalt())
