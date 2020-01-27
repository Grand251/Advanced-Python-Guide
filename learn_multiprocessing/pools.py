import os
import time
from multiprocessing import Pool


def simple_process(x):
    print(os.getpid())
    time.sleep(2)


# We can start up a pool of processes and map the to an iterable like so
with Pool(3) as pool:
    start = time.time()
    pool.map(simple_process, range(9))
    elapsed = time.time() - start

print('Elapsed: {}'.format(elapsed))

# ~6 Seconds is quite a bit better that the ~18 seconds it would
# have taken to run each iteration sequentially!
