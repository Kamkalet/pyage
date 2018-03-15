import logging
import os
import Pyro4

import matplotlib.pyplot as plt

from pyage.core.agent.aggregate import AggregateAgent
from pyage.core.emas import EmasService
from pyage.core.locator import GridLocator
from pyage.core.migration import ParentMigration
from pyage.core.stats.gnuplot import StepStatistics
from pyage.core.stop_condition import StepLimitStopCondition
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
from pyage.salesman.crossover import Crossover
from pyage.salesman.eval import TSPEvaluator
from pyage.salesman.mutation import Mutation
from pyage.salesman.naming_service import NamingService

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

agents_count = 3
logger.debug("EMAS, %s agents", agents_count)
agents = root_agents_factory(agents_count, AggregateAgent)

stop_condition = lambda: StepLimitStopCondition(7000)

agg_size = 20
aggregated_agents = EmasInitializer(gen(), size=agg_size, energy=20)
emas = EmasService
#
minimal_energy = lambda: 10
reproduction_minimum = lambda: 100
migration_minimum = lambda: 120
newborn_energy = lambda: 100
transferred_energy = lambda: 40


evaluation = lambda: TSPEvaluator()
crossover = lambda: Crossover(size=10)
mutation = lambda: Mutation(probability=0.2)

address_provider = address.SequenceAddressProvider

migration = ParentMigration
locator = GridLocator

stats = lambda: StepStatistics('fitness_%s_pyage.txt' % __name__)

naming_service = lambda: NamingService(starting_number=1)


## TODO move it to another file


# fig = plt.figure()
# ax = fig.add_subplot(111)
# x_points = xrange(0,9)
# y_points = xrange(0,9)
# p = ax.plot(x_points, y_points, 'b')
# ax.set_xlabel('x-points')
# ax.set_ylabel('y-points')
# ax.set_title('Simple XY point plot')
# plt.show()
