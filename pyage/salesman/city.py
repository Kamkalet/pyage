class City(object):
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "\nName: " + str(self.name) + " (" + str(self.x) + ", " + str(self.y) + ")"
