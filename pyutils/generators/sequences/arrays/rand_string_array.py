# generators/sequences/arrays/rand_int_array.py
import random
from generators.strings.rand_str import rand_string
import string

def rand_string_array(string_length : int, length: int, charachters = string.ascii_letters + string.digits + string.punctuation):
    rand_string_array = []
    for i in range(length):
        rand_string_array.append(rand_string(string_length, charachters))
    return rand_string_array


