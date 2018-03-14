import logging
import os
import Pyro4

from pyage.core import address
from pyage.core.agent.agent import generate_agents, Agent
from pyage.core.agent.aggregate import AggregateAgent
from pyage.core.locator import Locator
from pyage.core.migration import NoMigration
from pyage.core.statistics import SimpleStatistics
from pyage.core.emas import EmasService
from pyage.core.stop_condition import StepLimitStopCondition

import sys

from pyage.salesman.args_parser import get_args
from pyage.salesman.init import TSPInitializer, root_agents_factory, EmasInitializer
from pyage.salesman.town_generator import CityGenerator

logger = logging.getLogger(__name__)

# TODO to other file move it now or never
args = get_args()
if len(args) > 1:
    gen = CityGenerator(args[1])
else:
    gen = CityGenerator(None, 10)

# population_size = 50
# number_of_cities = 10
# initial = TSPInitializer(population_size, gen())
# print(str(initial.get_cities()))
# print(str(initial.get_population()))

agents_count = 2
logger.debug("EMAS, %s agents", agents_count)
agents = root_agents_factory(agents_count, AggregateAgent)

stop_condition = lambda: StepLimitStopCondition(100)

agg_size = 40
aggregated_agents = EmasInitializer(gen(), size=agg_size, energy=40)

emas = EmasService
#
minimal_energy = lambda: 10
reproduction_minimum = lambda: 100
migration_minimum = lambda: 120
newborn_energy = lambda: 100
transferred_energy = lambda: 40

budget = 0
evaluation = lambda: TSPEvaluator()
# crossover
# mutation
budget = 0

# crossover = lambda: Crossover(size=30)
# mutation = lambda: Mutation(probability=0.2, evol_probability=0.5)