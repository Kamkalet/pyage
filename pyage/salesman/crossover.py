import random
from pyage.core.operator import Operator
from pyage.salesman.genotype import TSPGenotype

import logging

logger = logging.getLogger(__name__)

class AbstractCrossover(Operator):
    def __init__(self, type, size):
        super(AbstractCrossover, self).__init__(type)
        self.__size = size

    def process(self, population):
        parents = list(population)
        for i in range(len(population), self.__size):
            p1, p2 = random.sample(parents, 2)
            genotype = self.cross(p1, p2)
            population.append(genotype)

class Crossover(AbstractCrossover):
    def __init__(self, size):
        super(Crossover, self).__init__(TSPGenotype, size)

    def cross(self, p1, p2):
        logger.debug("Crossing:\n{0}\nAND\n{1}".format(p1, p2))

        i = random.randrange(0, len(p1.chromosome))
        j = random.randrange(0, len(p1.chromosome))
        if i > j:
            i, j = j, i

        parent1RemovedTraits = p1.chromosome[i:j]
        parent2chromosom = p2.chromosome

        for city in parent1RemovedTraits:
            parent2chromosom.remove(city)

# should i shuffle ?
        offspring =   parent2chromosom + (parent1RemovedTraits)

        genotype = TSPGenotype(p1.cities)
        genotype.set_chromosome(offspring)

        logger.debug("Crossed genotype: " + str(genotype))

        return genotype
