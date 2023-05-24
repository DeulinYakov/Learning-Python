class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return (self.x + other.x, self.y + other.y)


a = Vector(4, 3)
b = Vector(1, 6)
print(a+b)
