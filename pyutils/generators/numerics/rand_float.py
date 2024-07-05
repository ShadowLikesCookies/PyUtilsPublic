import random

def rand_float(min_value : float, max_value: float) -> float:
    """
    Generates a random floating-point number within the specified range.
    
    Args:
        min_value (float): The minimum value for the random number (default is 0.0).
        max_value (float): The maximum value for the random number (default is 1.0).
    
    Returns:
        float: A random floating-point number within the specified range.
    """
    return random.uniform(min_value, max_value)