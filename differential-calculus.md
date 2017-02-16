# Differential calculus

## Limit

A limit is the value of a function approaches as we move to some x value.


## Limit at a point

The instantaneous rate of change of a function at a specific point.

**lim(h -> 0) [ f(x + h) - f(x) ] / h**


## Derivative

A derivative is the slope of a tangent line at a specific point. The derivative of a function f(x) is denoted as f’(x).

* **f'(x) > 0** when the function increases
* **f'(x) < 0** when the function decreases
* **f'(x) = 0** when in minima, maxima and inflection points


### Rules

* C' = 0
* d( Cf(x) ) = Cf'(x)
* d( f(x) + g(x) ) = f'(x) + g'(x)
* d( f(x)g(x) ) = f(x)g'(x) + f'(x)g(x)


### Specific functions

* dx<sup>n</sup> = nx<sup>n - 1</sup>
* log'(x) = 1/x
* e'<sup>x</sup> = e<sup>x</sup>
* ​sin'(x) = cos(x)
* ​cos'(x) = −sin(x)​


## Python

```python
from matplotlib import pyplot
import numpy

def f(x):
  return x * x + 3


dx = 0.05
interval = numpy.arange(0, 4, dx)
values = [f(x) for x in interval]
derivative = numpy.gradient(values, dx)

pyplot.plot(interval, values, label=r"f(x) = x$^2$ + 3")
pyplot.plot(interval, derivative, label="f'(x) = 2x")
pyplot.legend()
pyplot.show()
```
