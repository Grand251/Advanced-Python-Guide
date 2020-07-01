"""
This package focuses on how to test our code using mocks.
Pure functions that don't touch anything outside our system
are relatively easy to test, even if they interact with a
DB that you use for testing. If your system interacts with
a DB or service that you don't want to be affected every time
you run your tests, then you can mock out those pieces using
unittest.mock!
"""