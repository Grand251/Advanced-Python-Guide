import time
from unittest.mock import Mock, MagicMock


class Component:
    """A simple component of our system"""
    def do_something(self, num):
        """Component function that calls a [rivate function"""
        return self._do_something_else(num + 1)

    def _do_something_else(self, num):
        """Private function that returns the input + 1"""
        return num + 1

    def get_int_from_service(self):
        """Function that won't work in our testing apparatus"""
        raise Exception('Could not connect to blah blah...')


# We have our class. Let's do some testing!
component = Component()

print('First lets see what our components do_something function returns without any mocking ')
print('component.do_something(0) ->', component.do_something(0))

component._do_something_else = MagicMock(return_value=99)
print('After mocking: component.do_something(0) ->', component.do_something(0))

# The rest of our component still works as expected.
try:
    component.get_int_from_service()
except Exception as e:
    print('Our component raised an exception as expected:', e)

# So like we did with our private function, we can give our exeption raiseing function
component.get_int_from_service = MagicMock(return_value=22)

print('component.get_int_from_service() ->', component.get_int_from_service())

# Or we can even cause it to raise a different exception
component.get_int_from_service = MagicMock(side_effect=KeyError('New KeyError Exception'))

try:
    component.get_int_from_service()
except KeyError as e:
    print('New Exception: ', e)
