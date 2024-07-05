# generators/sequences/arrays/rand_int_array.py
import random



def rand_int_array(int1 : int, int2 : int, length: int):
    rand_int_array = []
    for i in range(length):
        rand_int_array.append(random.randint(int1, int2))
    return rand_int_array




