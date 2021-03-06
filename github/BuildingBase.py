class Building:
    def __init__(self, south, west, width_WE, width_NS, height=10):
        self.south = south
        self.west = west
        self.width_WE = width_WE
        self.width_NS = width_NS
        self.height = height

    def corners(self):
        corner = {}
        corner['north-east'] = [self.south + self.width_NS,self.west + self.width_WE]
        corner['south-east'] = [self.south,self.west + self.width_WE]
        corner['north-west'] = [self.south + self.width_NS,self.west]
        corner['south-west'] = [self.south,self.west]
        return corner

    def area(self):
        return self.width_NS * self.width_WE

    def volume(self):
        return self.width_NS * self.width_WE * self.height

    def __repr__(self):
        return ('Building({0.south}, {0.west}, {0.width_WE}, {0.width_NS}, {0.height})'.format(self))


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    def json_dict(d):
        return dict((k, list(v)) for k, v in d.items())

    b = Building(1, 2, 2, 3)
    b2 = Building(1, 2, 2, 3, 5)
    print(b.corners())
    print(b.area())
    print(b.volume())
    print(str(b))
    # assert json_dict(b.corners()) == {'north-east': [4, 4], 'south-east': [1, 4],
    #                                   'south-west': [1, 2], 'north-west': [4, 2]}, "Corners"
    # assert b.area() == 6, "Area"
    # assert b.volume() == 60, "Volume"
    # assert b2.volume() == 30, "Volume2"
    # assert str(b) == "Building(1, 2, 2, 3, 10)", "String"

