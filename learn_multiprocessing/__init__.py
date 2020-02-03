"""
This package focuses on the multiprocessing module. This module
allows us to spins up new processes to handle tasks asynchronously.
It takes a little longer to spin up a new process than an new thread,
but processes are not limited by the GIL (Global Interpreter Lock) either.
Python also implements some ways for you to share objects between processes,
so don't let anyone tell you that threads are better because the share the
same memory space! I recommend using multiprocessing for long running tasks/subroutines.
The APIs between multiprocessing and threading are very similar, so some topics will
only be covered in one or the other, even though they apply to both.

Simple example
    simple.py

How to construct a pool of processes to a repetitive task with an iterable of inputs
    pools.py

"""