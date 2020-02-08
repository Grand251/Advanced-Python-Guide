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


print('A:', A.mro())
print('B:', B.mro())
print('C:', C.mro())
