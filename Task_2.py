class Road:
    def __init__(self, _length, _width):
        self.length = _length
        self.width = _width

    def mass(self):
        return self.length * self.width

class MassCount(Road):
    def __init__(self, length, width, volume):
        super().__init__(length, width)
        self.volume = volume

r = MassCount(25, 10000, 125)
print(r.mass())