class Coordinate:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Coordinate(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def value_x(self, x=None) -> int:
        if x is not None:
            self.x = x
        return int(self.x)

    def value_y(self, y=None) -> int:
        if y is not None:
            self.y = y
        return int(self.y)
