import math

from ._global import EPSILON


class Vector:
    def __init__(self, lst):
        self._values = list(lst)

    @classmethod
    def zero(cls, dim):
        return cls([0] * dim)

    def norm(self):
        return math.sqrt(sum(e ** 2 for e in self))

    def dot(self, another):
        assert len(self) == len(another), \
            "Error in dot product. Length of vector must be same."
        return sum(a * b for a, b in zip(self, another))

    def normalize(self):
        if self.norm() < EPSILON:
            raise ZeroDivisionError("Normalize error! norm is zero.")
        return Vector(self._values) / self.norm()

    def __truediv__(self, other):
        return (1 / other) * self

    def __getitem__(self, item):
        return self._values[item]

    def __add__(self, other):
        assert len(self._values) == len(other), \
            "Error  in adding. Length of vector must be same."
        return Vector([a + b for a, b in zip(self._values, other)])

    def __sub__(self, other):
        assert len(self) == len(other), \
            "Error  in subtracting. Length of vector must be same."
        return Vector([a - b for a, b in zip(self, other)])

    def __pos__(self):
        return 1 * self

    def __neg__(self):
        return -1 * self

    def __mul__(self, k):
        return Vector([k * e for e in self])

    def __rmul__(self, other):
        return self * other

    def __iter__(self):
        return self._values.__iter__()

    def __len__(self):
        return len(self._values)

    def __repr__(self):
        return "Vector({})".format(self._values)

    def __str__(self):
        return "({})".format(", ".join([str(e) for e in self._values]))
