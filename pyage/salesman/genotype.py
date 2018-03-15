import random
import math


class TSPGenotype(object):
    def __init__(self, cities):
        # list of City objects
        self.cities = cities
        self.number_of_cities = len(cities)
        # chromosome - fx. list [1,6,4] indicates that salesman goes from 1 to 6 to 4 and back to 1
        self.chromosome = [x for x in xrange(0, self.number_of_cities)]
        random.shuffle(self.chromosome)
        self.fitness = self.get_fitness()

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "\nTSPGenotype{list=" + str(self.chromosome) + ", fitness=" + str(self.fitness) + "}"

    def get_fitness(self):
        fitness = 0.0
        prev = self.chromosome[0]
        for i in xrange(0, self.number_of_cities):
            j = self.chromosome[i]
            xvector = self.cities[j].x - self.cities[prev].x
            yvector = self.cities[j].y - self.cities[prev].y
            fitness -= math.sqrt(math.pow(xvector, 2) + math.pow(yvector, 2))
            prev = j
        return fitness

    def set_chromosome(self, new_chromosome):
        self.chromosome = new_chromosome
        self.fitness = self.get_fitness()
