"""
You can implement your own implementations by implementing
__copy__() and __deepcopy__() in your classes.
"""
import uuid
import copy

# Let's use the same classes from shallow_vs_deep, but implement
# __copy__ and __deepcopy__


class Address:
    def __init__(self, city: str, state: str):
        self.city = city
        self.state = state


class Account:
    def __init__(self, address: Address):
        self.id = uuid.uuid4()
        self.address = address

    def __copy__(self):
        """Give shallow copies an is_copy flag"""
        new = type(self)(self.address)
        new.id = self.id
        new.is_copy = True
        return new

    def __deepcopy__(self, memodict={}):
        """Make deep copies reference the original address"""
        new = type(self)(self.address)
        return new


address = Address(city='Colorado Springs', state='Colorado')
account = Account(address)

print('Shallow Copy - Give shallow copy an is_copy flag \n')
shallow_copied_account = copy.copy(account)

print('account:')
print(vars(account))

print()
print('shallow_copied_account: ')
print(vars(shallow_copied_account))

print(); print()
print('Deep Copy - Make seep copy use original address reference.')

deep_copied_account = copy.deepcopy(account)

print('account:')
print(vars(account))

print('deep_copied_account: ')
print(vars(deep_copied_account))
