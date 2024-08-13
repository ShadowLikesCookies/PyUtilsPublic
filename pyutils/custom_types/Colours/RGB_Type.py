class RGB:
    def __init__(self, r: int, g: int, b: int) -> None:
        if isinstance(r, int):
            if r >= 0 and r <= 255:
                self.r = r
            else: raise ValueError("Number must be between 0 and 255")
        else: raise TypeError("TypeError: Value must be a Int")

        if isinstance(g, int):
            if g >= 0 and g <= 255:
                self.g = g
            else: raise ValueError("Number must be between 0 and 255")
        else: raise TypeError("TypeError: Value must be a Int")

        if isinstance(b, int):
            if b >= 0 and b <= 255:
                self.b = b
            else: raise ValueError("Number must be between 0 and 255")
        else: raise TypeError("TypeError: Value must be a Int")


    def __repr__(self) -> str:
        return f"RGB(Red: {self.r}, Green: {self.g}, Blue: {self.b})"
        
print(
RGB(1,2,3))/