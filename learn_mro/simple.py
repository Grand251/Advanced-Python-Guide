"""
The following is a simple example of the MRO, and how we can
it without having to do the algorithm ourselves.
"""


class A:
    pass


class B(A):
    pass


class C(B):
    pass


print('A.mro():', A.mro())
print('B.mro():', B.mro())
print('C.mro():', C.mro())
