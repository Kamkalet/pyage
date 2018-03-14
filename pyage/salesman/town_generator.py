import random

from pyage.salesman.city import City


# if a file is not given, it will generate new cities and write to file
class CityGenerator:
    def __init__(self, file_name=None, number_of_cities=10):
        self.file_name = file_name
        self.number_of_cities = number_of_cities
        if file_name is None:
            self.cities = self.generate_random_cities()
            self.write_to_file("./cities.csv")
        else:
            self.cities = self.get_from_file()

    def __call__(self):
        return self.cities

    def generate_random_cities(self):
        cities = []
        for i in xrange(self.number_of_cities):
            cities.append(City("City " + str(i), random.randint(0, 100), random.randint(0, 100)))
        return cities

    def get_from_file(self):
        with open(self.file_name, "r") as ins:
            cities = []
            for line in ins:
                name, x, y = line.strip().split(",")
                cities.append(City(name, int(x), int(y)))
        return cities

    def write_to_file(self, file_name):
        file_desc = open(file_name, "w+")
        for city in self.cities:
            line = city.name + "," + str(city.x) + "," + str(city.y)
            file_desc.write(line + "\n")
        file_desc.flush()
