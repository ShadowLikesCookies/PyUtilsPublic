import sys
import os

current = os.path.dirname(os.path.realpath(__file__))

parent = os.path.dirname(current)

vector_types_dir = os.path.join(parent, 'VectorTypes')

sys.path.append(vector_types_dir)
from Vector4 import Vector4 
def test_vector4():
    # Test initialization
    v1 = Vector4(3, 4, 5, 6)
    assert v1.x == 3.0, "Initialization failed for x"
    assert v1.y == 4.0, "Initialization failed for y"
    assert v1.z == 5.0, "Initialization failed for z"
    assert v1.w == 6.0, "Initialization failed for w"

    # Test __repr__
    assert repr(v1) == "Vector4(3.0, 4.0, 5.0, 6.0)", "__repr__ failed"

    # Test __len__
    assert len(v1) == 4, "__len__ failed"

    # Test __eq__
    v2 = Vector4(3, 4, 5, 6)
    assert v1 == v2, "__eq__ failed for equal vectors"
    v3 = Vector4(1, 2, 3, 4)
    assert v1 != v3, "__eq__ failed for unequal vectors"

    # Test __add__
    v4 = v1 + v2
    assert repr(v4) == "Vector4(6.0, 8.0, 10.0, 12.0)", "__add__ failed"

    # Test __sub__
    v5 = v1 - v3
    assert repr(v5) == "Vector4(2.0, 2.0, 2.0, 2.0)", "__sub__ failed"

    # Test __mul__
    v6 = v1 * v2
    assert repr(v6) == "Vector4(9.0, 16.0, 25.0, 36.0)", "__mul__ failed"

    # Test __truediv__
    v7 = v1 / v2
    assert repr(v7) == "Vector4(1.0, 1.0, 1.0, 1.0)", "__truediv__ failed"

    # Test __neg__
    v8 = -v1
    assert repr(v8) == "Vector4(-3.0, -4.0, -5.0, -6.0)", "__neg__ failed"

    # Test __abs__
    assert abs(v1) == (3.0**2 + 4.0**2 + 5.0**2 + 6.0**2) ** 0.5, "__abs__ failed"

    # Test __setitem__ and __getitem__
    v1[0] = 5
    assert v1[0] == 5.0, "__setitem__ failed for x"
    v1[1] = 6
    assert v1[1] == 6.0, "__setitem__ failed for y"
    v1[2] = 7
    assert v1[2] == 7.0, "__setitem__ failed for z"
    v1[3] = 8
    assert v1[3] == 8.0, "__setitem__ failed for w"

    # Test __contains__
    assert 5.0 in v1, "__contains__ failed for existing value"
    assert 10.0 not in v1, "__contains__ failed for non-existing value"

    # Test __hash__
    v9 = Vector4(3, 4, 5, 6)
    assert hash(v1) == hash(v9), "__hash__ failed"

    # Test __copy__ and __deepcopy__
    v10 = v1.__copy__()
    assert v10 == v1, "__copy__ failed"
    
    import copy
    v11 = copy.deepcopy(v1)
    assert v11 == v1, "__deepcopy__ failed"

    print("All tests passed!")

test_vector4()
