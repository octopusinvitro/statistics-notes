import numpy


class Maximum:
    def __init__(self, samples):
        self.name = 'Maximum'
        self.value = numpy.max(samples)
        self.rounded = round(self.value, 2)
