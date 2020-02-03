"""
This package focuses on the threading module.
This module is particularly useful for spinning
off asynchronous tasks in a simple and easy to use way.
While the GIL (Global Interpreter Lock) only allows one thread
the execute at a time, threads are still particularly useful
for tasks that require a lot of waiting,like http requests or
database transactions. For computationally expensive applications,
checkout the multiprocessing module. The APIs for threading and
multiprocessing are very similar, so why not learn both!

Simple example of how to use threads
    simple.py

Example of how to use primitive thread locks
    locks.py
"""