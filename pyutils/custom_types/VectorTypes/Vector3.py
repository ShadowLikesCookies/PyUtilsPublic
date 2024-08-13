import copy

class Vector3:
    def __init__(self, x: float, y: float, z: float) -> None:
        self._x = float(x)
        self._y = float(y)
        self._z = float(z)

    @property
    def x(self) -> float:
        return self._x

    @x.setter
    def x(self, value: float) -> None:
        if not isinstance(value, (int, float)):
            raise TypeError(f"x must be an int or float, got {type(value).__name__}")
        self._x = float(value)

    @property
    def y(self) -> float:
        return self._y

    @y.setter
    def y(self, value: float) -> None:
        if not isinstance(value, (int, float)):
            raise TypeError(f"y must be an int or float, got {type(value).__name__}")
        self._y = float(value)

    @property
    def z(self) -> float:
        return self._z

    @z.setter
    def z(self, value: float) -> None:
        if not isinstance(value, (int, float)):
            raise TypeError(f"z must be an int or float, got {type(value).__name__}")
        self._z = float(value)

    def __repr__(self) -> str:
        return f"Vector3({self.x}, {self.y}, {self.z})"

    def __len__(self) -> int:
        return 3

    def __eq__(self, other: 'Vector3') -> bool:
        if not isinstance(other, Vector3):
            return NotImplemented
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __add__(self, other: 'Vector3') -> 'Vector3':
        return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other: 'Vector3') -> 'Vector3':
        return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other: 'Vector3') -> 'Vector3':
        return Vector3(self.x * other.x, self.y * other.y, self.z * other.z)

    def __truediv__(self, other: 'Vector3') -> 'Vector3':
        return Vector3(round(self.x / other.x, 3), round(self.y / other.y, 3), round(self.z / other.z, 3))

    def __neg__(self) -> 'Vector3':
        return Vector3(-self.x, -self.y, -self.z)

    def __abs__(self) -> float:
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5

    def __setitem__(self, index: int, value: float) -> None:
        if index == 0:
            self.x = value
        elif index == 1:
            self.y = value
        elif index == 2:
            self.z = value
        else:
            raise IndexError("Index must be 0, 1, or 2")

    def __contains__(self, value: float) -> bool:
        try:
            value = float(value)
            return value == self.x or value == self.y or value == self.z
        except ValueError:
            print("Vector3 can only contain floats. Query with either int or float.")

    def __hash__(self) -> int:
        return hash((self.x, self.y, self.z))

    def __getitem__(self, index: int) -> float:
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        elif index == 2:
            return self.z
        else:
            raise IndexError("Index must be 0, 1, or 2")

    def __copy__(self) -> 'Vector3':
        return Vector3(self.x, self.y, self.z)

    def __deepcopy__(self, memo: dict) -> 'Vector3':
        return Vector3(copy.deepcopy(self.x, memo), copy.deepcopy(self.y, memo), copy.deepcopy(self.z, memo))