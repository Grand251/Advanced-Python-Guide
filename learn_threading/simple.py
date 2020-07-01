"""Threading examples"""

import time
import threading


def simple_thread(arg):
    print("IN - simple_thread({})".format(arg))

    # Do stuff
    time.sleep(2)

    print('OUT - Simple Thread')


# Designate function for thread to execute, and supply arguments
thread = threading.Thread(target=simple_thread, args=('123', ))

# Start the thread.
thread.start()

# That's it! The thread is started and will execute until completion.
# Thanks to the GIL (Global Interpreter Lock), only one of our threads will
# execute at a time, which frees us up from worrying about most race conditions.
# If true parallelism is necessary, checkout the multiprocessing module.
#
# Lets check out what else we can do with our thread object.

thread.join()


# Luckily the GIL doesn't hold us up very much for threads that have to do a
# lot of waiting. Not that if we were to run simple_thread three times sequentially,
# it would take about 6 seconds.
threads = [threading.Thread(target=simple_thread, args=(x, )) for x in range(3)]

start = time.time()
for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

elapsed = time.time() - start
print('Time for all 3 three threads to finish: {}'.format(elapsed))

# Just about right at 2 seconds! Threading works great when you threads
# have to do some waiting. If our threads are computationally heavy, then
# we won't actually save all that much time due to the GIL restricting us to
# one thread at a time. For these situations, we can either use multiprocessing
# for long-running processes (they have to be long enough to negate the slow
# process startup time) or we can write extensions in C that escape the GIL. The
# latter scenario is usually unnecessary since there are so many third party
# packages that have already done the leg work. NumPy is one such package, that
# facilitates mathematical computations at the speed of C!
