import random

def rand_byte_array(length):
    """
    Generate a random byte array of the specified length.

    Args:
        length (int): The length of the byte array to generate.

    Returns:
        bytes: A random byte array.
    """
    byte_array = bytearray(random.getrandbits(8) for _ in range(length))
    return bytes(byte_array)
