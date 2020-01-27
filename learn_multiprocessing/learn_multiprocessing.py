"""Multiprocessing examples"""

import time
import multiprocessing

# Start a simple process that will execute until completion
def simple_process():
    print('Starting simple process')

    # Do some stuff
    time.sleep(5)

    print('End simple process')