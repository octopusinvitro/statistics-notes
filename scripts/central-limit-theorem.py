# -----------------------------------------#
# Rerenced in "sampling-distributions.md"  #
# -----------------------------------------#
import numpy
from matplotlib import pyplot
from scipy.stats import norm


mean = 10
deviation = 10
population = numpy.random.normal(mean, deviation, size=100000)
# population = numpy.random.poisson(mean, size=100000)

size = 30
means = []
for _ in range(500):
    samples = numpy.random.choice(population, size, replace=False)
    means.append(numpy.mean(samples))

means_mean = round(numpy.mean(means), 3)

mu = numpy.mean(population)
sigma = numpy.std(population) / (size**.5)
x = numpy.linspace(mu - 3 * sigma, mu + 3 * sigma, 100)
normal_distribution = norm.pdf(x, mu, sigma)

pyplot.figure(figsize=(15, 8))

pyplot.subplot(121)
pyplot.hist(population, bins=100, density=True, ec='steelblue')
pyplot.axvline(mean, color='r', linestyle='dashed')
pyplot.title(f'Population Mean: {mean}')
pyplot.xlabel('')

pyplot.subplot(122)
pyplot.hist(means, bins=20, density=True, ec='steelblue')
pyplot.plot(x, normal_distribution, color='k', label='normal PDF')
pyplot.title(f'Sampling Distribution Mean: {means_mean}')
pyplot.xlabel('')

pyplot.tight_layout()
pyplot.show()
