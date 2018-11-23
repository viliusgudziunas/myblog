import os

class Config(object):
    """Configuration class"""
    SECRET_KEY = os.environ.get("SECRET_KEY") or "you will never_guess"
