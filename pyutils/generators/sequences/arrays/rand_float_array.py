# generators/sequences/arrays/rand_int_array.py
import random
from generators.numerics.rand_float import rand_float

def rand_float_array(float1 : float, float2 : float, length: int):
    rand_float_array = []
    for i in range(length):
        rand_float_array.append(rand_float(float1, float2))
    return rand_float_array


