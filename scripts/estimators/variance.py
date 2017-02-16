import numpy


class Variance:
    def __init__(self, samples):
        self.name = 'Variance'
        self.value = numpy.var(samples)
        self.rounded = round(self.value, 2)
