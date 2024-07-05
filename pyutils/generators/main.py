from sequences.arrays.rand_int_array import randint_array
class generators:
    def __init__(self):
        pass

    def randinit_array(self, int1 : int, int2 : int, length : int):
        return randint_array(int1, int2, length)
    

generator = generators()

var = generator.randinit_array(0,1,5)
print(var)