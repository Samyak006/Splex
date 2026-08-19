import bcrypt

def hash_pass(password: str) -> str:
    """Hash a password using bcrypt.

    Args:
        password (str): The password to hash.

    Returns:
        str: The hashed password.
    """
    # Generate a salt
    salt = bcrypt.gensalt()
    # Hash the password
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed.decode('utf-8')

def verify_pass(password: str, hashed: str) -> bool:
    """Verify a password against a hashed password.

    Args:
        password (str): The password to verify.
        hashed (str): The hashed password to compare against.

    Returns:
        bool: True if the password matches the hash, False otherwise.
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))