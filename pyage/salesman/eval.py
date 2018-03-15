from pyage.salesman.genotype import TSPGenotype

from pyage.core.operator import Operator


class TSPEvaluator(Operator):
    def __init__(self):
        super(TSPEvaluator, self).__init__(TSPGenotype)


    def process(self, population):
        for genotype in population:
            genotype.fitness = self.evaluate(genotype)

    def evaluate(self, genotype):
        return genotype.get_fitness()
