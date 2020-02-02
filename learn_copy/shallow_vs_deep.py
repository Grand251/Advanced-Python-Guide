"""
Shallow Copy - Create new object, but use same references.
Deep Copy    - Create new object and deep copies of references.
"""


import copy
import uuid


class Address:
    def __init__(self, city: str, state: str):
        self.city = city
        self.state = state


class Account:
    def __init__(self, address: Address):
        self.id = uuid.uuid4()
        self.address = address


address = Address(city='Denver', state='Colorado')
account = Account(address=address)

print('Original account: {}'.format(id(account)))
print('Original account.address: {}'.format(id(account.address)))

# Shallow Copy
shallow_copied_account = copy.copy(account)

print()
print('Shallow copied account: {}'.format(id(shallow_copied_account)))
print('Shallow copied account.address: {}'.format(id(shallow_copied_account.address)))

# Notice that the shallow_copied_account.address is the same as the original.

print()
print('id(account) == id(shallow_copied_account): ' +
      str(id(account) == id(shallow_copied_account)))
print('id(account.address) == id(shallow_copied_account.address): ' +
      str(id(account.address) == id(shallow_copied_account.address)))

# If we want the referenced objects copied too, we can use deepcopy

deep_copied_account = copy.deepcopy(account)

print()
print('Deep copied account: {}'.format(id(deep_copied_account)))
print('Deep copied account.address: {}'.format(id(deep_copied_account)))

print()
print('id(account) == id(deep_copied_account): ' +
      str(id(account) == id(deep_copied_account)))
print('id(account.address) == id(deep_copied_account.address): ' +
      str(id(account.address) == id(deep_copied_account.address)))
