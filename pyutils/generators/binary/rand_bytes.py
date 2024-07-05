import random

def rand_byte_binary():
    """
    Generate a random byte as a binary string.

    Returns:
        str: A random byte value as a binary string.
    """
    byte_value = random.randint(0, 255)
    return format(byte_value, '#010b')