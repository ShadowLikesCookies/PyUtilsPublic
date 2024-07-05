import random

def rand_complex(real_min : float, real_max : float, imag_min : float, imag_max : float) -> complex:
    """
    Generates a random complex number within the specified ranges.
    
    Args:
        real_min (float): Minimum value for the real part (default: -10).
        real_max (float): Maximum value for the real part (default: 10).
        imag_min (float): Minimum value for the imaginary part (default: -10).
        imag_max (float): Maximum value for the imaginary part (default: 10).
    
    Returns:
        complex: A random complex number.
    """
    real = random.uniform(real_min, real_max)
    imag = random.uniform(imag_min, imag_max)
    return complex(real, imag)