# generators/sequences/arrays/rand_int_array.py
import random
from generators.numerics.rand_complex import rand_complex

def rand_complex_array(real_min : float, real_max : float, imag_min : float, imag_max : float, length : int):
    rand_complex_array = []
    for i in range(length):
        rand_complex_array.append(rand_complex(real_min, real_max, imag_min, imag_max))
    return rand_complex_array



