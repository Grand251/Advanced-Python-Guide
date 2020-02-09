
class A:
    VAL = 'A'


class B(A):
    VAL = 'B'


class C(B):
    def get_b(self):
        # Super with no arguments returns a proxy object of the parent class
        return super().VAL

    def get_a(self):
        # Super can also specify a class to use.
        return super(B, self).VAL


print('class C: super().VAL:', C().get_b())
print('class C: super(B, self).VAL', C().get_a())

print()


# Super can also be used on classes that inherit from mutliple classes
class Base1:
    VAL = 1


class Base2:
    VAL = 2


class Sub(Base1, Base2):
    def get_val(self):
        return super().VAL


print("Notice the base class on the left is used first")
print('class Sub: super().VAL', Sub().get_val())
print('Sub MRO:', Sub.mro())
