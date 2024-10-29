# utils.py (or any appropriate file)
from .models import Organization

def is_organization(user):
    """Check if the user is an Organization."""
    return isinstance(user, Organization)
