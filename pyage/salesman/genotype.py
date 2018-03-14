import random


class TSPGenotype(object):
    def __init__(self, cities):
        self.cities = cities
        self.city_count = len(cities)
        self.list = [x for x in xrange(0, self.city_count)]
        random.shuffle(self.list)
        self.fitness = self.get_fitness()

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "\nTSPGenotype{list=" + str(self.list) + ", fitness=" + str(self.fitness) + "}"

    def get_fitness(self):
        fitness = 0.0
        prev = self.list[0]
        for i in xrange(1, self.city_count + 1):
            i %= self.city_count
            index = self.list[i]
            delta_x = self.cities[index].x - self.cities[prev].x
            delta_y = self.cities[index].y - self.cities[prev].y
            fitness -= delta_x ** 2 + delta_y ** 2
            prev = index
        return fitness

    def set_list(self, list):
        self.list = list[:]
        self.fitness = self.get_fitness()
