# -----------------------------------------#
# Rerenced in "sampling-distributions.md"  #
# -----------------------------------------#
import numpy
from matplotlib import pyplot

from estimators.maximum import Maximum
from estimators.mean import Mean
from estimators.variance import Variance

Estimator = Maximum

mean, deviation = 50, 15
population = numpy.random.normal(mean, deviation, 100000)

statistics = []
size = 6
for _ in range(500):
    samples = numpy.random.choice(population, size, replace=False)
    statistics.append(Estimator(samples).value)

pyplot.figure(figsize=(15, 8))

statistic = Estimator(population)
pyplot.subplot(121)
pyplot.hist(population, bins=100, density=True, ec='steelblue')
pyplot.axvline(statistic.value, color='r', linestyle='dashed')
pyplot.title(f'Population {statistic.name}: {statistic.rounded}')
pyplot.xlabel('Population distribution')

statistic = Estimator(statistics)
pyplot.subplot(122)
pyplot.hist(statistics, bins=20, density=True, ec='steelblue')
pyplot.axvline(statistic.value, color='r', linestyle='dashed')
pyplot.title(f'Sampling Distribution of the {statistic.name} \nMean: {statistic.rounded}')
pyplot.xlabel(f'Sample {statistic.name} distribution')

pyplot.tight_layout()
pyplot.show()
