"""
Create a Vector object that supports addition, subtraction, dot products, and norms. So, for example:

a = Vector([1, 2, 3])
b = Vector([3, 4, 5])
c = Vector([5, 6, 7, 8])

a.add(b)      # should return a new Vector([4, 6, 8])
a.subtract(b) # should return a new Vector([-2, -2, -2])
a.dot(b)      # should return 1*3 + 2*4 + 3*5 = 26
a.norm()      # should return sqrt(1^2 + 2^2 + 3^2) = sqrt(14)
a.add(c)      # raises an exception
If you try to add, subtract, or dot two vectors with different lengths, you must throw an error!

Also provide:

a toString method, so that using the vectors from above, a.toString() === '(1,2,3)' (in Python, this is a __str__ method, so that str(a) == '(1,2,3)')
an equals method, to check that two vectors that have the same components are equal
Note: the test cases will utilize the user-provided equals method.
"""


def validate_vectors(method):
    def wrapper(self, obj):
        if len(self.lst) != len(obj.lst):
            raise ValueError("Vector lengths do not match")
        return method(self, obj)

    return wrapper


class Vector:
    def __init__(self, lst: list) -> None:
        self.lst = lst

    @validate_vectors
    def add(self, obj):
        return Vector([self.lst[i] + obj.lst[i] for i in range(len(self.lst))])

    @validate_vectors
    def subtract(self, obj):
        return Vector([self.lst[i] - obj.lst[i] for i in range(len(self.lst))])

    @validate_vectors
    def dot(self, obj):
        return sum([self.lst[i] * obj.lst[i] for i in range(len(self.lst))])

    def norm(self):
        return sum(x**2 for x in self.lst)**0.5

    def __str__(self):
        return "(" + ",".join(str(x) for x in self.lst) + ")"

    def equals(self, obj):
        return self.lst == obj.lst
