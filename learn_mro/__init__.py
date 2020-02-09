"""
MRO - Method Resolution Order

The MRO is how python know which inherited method to use on classes where,
the method has not been overwritten. This is naive for classes that only
inherit from one base class, but python allows multiple inheritance.
This can make inheritance a little more complicated than most of us are used
to, therefore, we need to know more about the MRO. This plays an important role
when dealing with complex inheritance patterns. Modern Python uses th C3 algorithm.

"""