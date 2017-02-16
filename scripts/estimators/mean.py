import numpy


class Mean:
    def __init__(self, samples):
        self.name = 'Mean'
        self.value = numpy.mean(samples)
        self.rounded = round(self.value, 2)
