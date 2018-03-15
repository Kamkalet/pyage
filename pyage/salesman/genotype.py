import random
import math


class TSPGenotype(object):
    def __init__(self, cities):
        # list of City objects
        self.cities = cities
        self.city_count = len(cities)
        #chromosome - fx. list [1,6,4] indicates that salesman goes from 1 to 6 to 4 and back to 1
        self.chromosome = [x for x in xrange(0, self.city_count)]
        random.shuffle(self.chromosome)
        self.fitness = self.get_fitness()

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "\nTSPGenotype{list=" + str(self.chromosome) + ", fitness=" + str(self.fitness) + "}"

    def get_fitness(self):
        fitness = 0.0
        prev = self.chromosome[0]
        for i in xrange(1, self.city_count + 1):
            i %= self.city_count
            index = self.chromosome[i]
            delta_x = self.cities[index].x - self.cities[prev].x
            delta_y = self.cities[index].y - self.cities[prev].y
            fitness -= math.sqrt(delta_x ** 2 + delta_y ** 2)
            prev = index
        return fitness

    def set_chromosom(self, list):
        self.chromosome = list[:]
        self.fitness = self.get_fitness()
