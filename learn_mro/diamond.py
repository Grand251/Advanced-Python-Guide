"""
Python allows diamond inheritance, and normally works as expected.
The following is a simple example of diamond inheritance.
"""

class A:
    """Base class that only inherits from object"""
    VAL = 'A'


class B(A):
    """Inherits A"""
    VAL = 'B'


class C(A):
    """Inherits A"""
    VAL = 'C'
    pass


class D(B, C):
    """Inherits both B and C, but will prefer B"""
    pass


print('D.VAL:', D.VAL)
print('D MRO: ', D.mro(), '\n')

# But C3 cannot resolve all patterns.
# The following class definition throws a TypeError

try:

    class E(A, C):
        pass

except TypeError as e:
    print('The C3 algorithm cannot resolve the inheritance pattern for: class E(A, C)')
    print('TypeError:', str(e).replace('\n', ' '))
