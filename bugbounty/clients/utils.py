# utils.py (or any appropriate file)
from .models import User

def is_client(user):
    """Check if the user is a Client."""
    return isinstance(user, User)
