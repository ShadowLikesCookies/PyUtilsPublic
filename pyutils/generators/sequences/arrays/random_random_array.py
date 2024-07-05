import random
from generators.strings.rand_str import rand_string
from generators.numerics.rand_bool import rand_bool
from generators.numerics.rand_float import rand_float
from generators.numerics.rand_int import rand_int
from generators.numerics.rand_complex import rand_complex

def rand_random_array(length, use_str=True, use_bool=True, use_float=True, use_int=True, use_complex=True):
    """
    Generate a random array of mixed data types.

    Args:
        length (int): The length of the array to generate.
        use_str (bool, optional): Whether to include strings in the array. Defaults to True.
        use_bool (bool, optional): Whether to include booleans in the array. Defaults to True.
        use_float (bool, optional): Whether to include floats in the array. Defaults to True.
        use_int (bool, optional): Whether to include integers in the array. Defaults to True.
        use_complex (bool, optional): Whether to include complex numbers in the array. Defaults to True.

    Returns:
        list: A random array of mixed data types.
    """
    random_array = []
    for _ in range(length):
        data_type = random.choice(['str', 'bool', 'float', 'int', 'complex'])
        if data_type == 'str' and use_str:
            random_array.append(rand_string(50))
        elif data_type == 'bool' and use_bool:
            random_array.append(rand_bool())
        elif data_type == 'float' and use_float:
            random_array.append(rand_float(0.000000000000000001, 500000000.0))
        elif data_type == 'int' and use_int:
            random_array.append(rand_int(0, 1000000000000000))
        elif data_type == 'complex' and use_complex:
            random_array.append(rand_complex(0.000000000000000001, 500000000000.0, 0.0000000000000000000000001, 100000000000000000000000.0))
    return random_array


print(rand_random_array(50))