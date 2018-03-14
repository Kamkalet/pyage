from pyage.core.operator import Operator
from pyage.core.emas import EmasAgent
from pyage.core.operator import Operator
from pyage.salesman.city import City
from pyage.salesman.genotype import TSPGenotype
from pyage.core.inject import Inject

import random


class EmasInitializer(object):
    def __init__(self, cities, energy, size):
        self.cities = cities
        self.energy = energy
        self.size = size

    @Inject("naming_service")
    def __call__(self):
        agents = {}
        for i in range(self.size):
            agent = EmasAgent(TSPGenotype(self.cities), self.energy, self.naming_service.get_next_agent())
            agents[agent.get_address()] = agent
        return agents


class TSPInitializer(Operator):
    def __init__(self, population_size, cities):
        super(TSPInitializer, self).__init__(TSPGenotype)
        self.size = population_size
        self.cities = cities
        self.population = self.generate_population(self.size, self.cities)

    def get_population(self):
        return self.population

    def get_cities(self):
        return self.cities

    def process(self, population):
        for i in range(self.size):
            population.append(self.population[i])

    def generate_population(self, number_of_genotypes, cities):
        return [TSPGenotype(cities) for _ in xrange(0, number_of_genotypes)]


def root_agents_factory(count, type):
    def factory():
        agents = {}
        for i in range(count):
            agent = type('R' + str(i))
            agents[agent.get_address()] = agent
        return agents

    return factory

