class Point:
    def __new__(cls, *args, **kwargs):
        print(f'Calling _new_ for {cls}')
        return super().__new__(cls)

    def __init__(self, x=0, y=0):
        print(f'Calling _new_ for {self}')
        self.x = x
        self.y = y


p1 = Point(1, 2)
