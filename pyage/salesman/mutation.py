import logging
import random
from pyage.core.operator import Operator
from pyage.salesman.genotype import TSPGenotype

logger = logging.getLogger(__name__)



class AbstractMutation(Operator):
    def __init__(self, type=TSPGenotype, probability=0.5):
        super(AbstractMutation, self).__init__(type)
        self.probability = probability

    def process(self, population):
        for genotype in population:
            if random.random() < self.probability:
                self.mutate(genotype)


class Mutation(AbstractMutation):
    def __init__(self, probability):
        super(Mutation, self).__init__(TSPGenotype, probability)

    def mutate(self, genotype):
        logger.debug("Mutating genotype: {0}".format(genotype))

        chromosome = genotype.chromosome[:]
        index1 = random.randrange(0, len( chromosome))
        index2 = random.randrange(0, len( chromosome))
        chromosome[index1],  chromosome[index2] = chromosome[index2],  chromosome[index1]
        gen = TSPGenotype(genotype.cities)
        gen.set_chromosom(chromosome)

        logger.debug("Mutated (rand swap) genotype: " + str(gen))

        return gen





