import copy

class Vector2:
    def __init__(self, x: float, y: float) -> None:
        self._x = float(x)
        self._y = float(y)

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

    def __repr__(self) -> str:
        return f"Vector2({self.x}, {self.y})"

    def __len__(self) -> int:
        return 2

    def __eq__(self, other: 'Vector2') -> bool:
        if not isinstance(other, Vector2):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def __add__(self, other: 'Vector2') -> 'Vector2':
        return Vector2(self.x + other.x, self.y + other.y)

    def __sub__(self, other: 'Vector2') -> 'Vector2':
        return Vector2(self.x - other.x, self.y - other.y)

    def __mul__(self, other: 'Vector2') -> 'Vector2':
        return Vector2(self.x * other.x, self.y * other.y)

    def __truediv__(self, other: 'Vector2') -> 'Vector2':
        return Vector2(round(self.x / other.x, 43), round(self.y / other.y, 3))

    def __neg__(self) -> 'Vector2':
        return Vector2(-self.x, -self.y)

    def __abs__(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __setitem__(self, index: int, value: float) -> None:
        if index == 0:
            self.x = value
        elif index == 1:
            self.y = value
        else:
            raise IndexError("Index must be 0 or 1")

    def __contains__(self, value: float) -> bool:
        try:
            value = float(value)
            return value == self.x or value == self.y
        except ValueError:
            print("Vector2 can only contain floats. Query with either int or float.")

    def __hash__(self) -> int:
        return hash((self.x, self.y))

    def __getitem__(self, index: int) -> float:
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        else:
            raise IndexError("Index must be 0 or 1")

    def __copy__(self) -> 'Vector2':
        return Vector2(self.x, self.y)

    def __deepcopy__(self, memo: dict) -> 'Vector2':
        return Vector2(copy.deepcopy(self.x, memo), copy.deepcopy(self.y, memo))
    