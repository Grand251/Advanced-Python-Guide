"""Simple multiprocessing example"""

import os
import time
import multiprocessing


# Define our process instructions
def simple_process(arg):
    print('Starting simple process wih arg: {}'.format(arg))

    # Do some stuff
    time.sleep(3)

    print('End simple process')


# Define the process and the function it will execute
process = multiprocessing.Process(target=simple_process, args=('Hello', ))

# Start the process
process.start()

# That's it! This is the minimum the get an additional process up and running.
# But, there are a couple of additional things we can do.

print('Original Process ID: ' + str(os.getpid()))
print('Child Process ID: ' + str(process.pid))
print('Process still running: ' + str(process.is_alive()))
print('Process is a daemon: ' + str(process.daemon))

# process.join() always returns None, and doesn't throw an exception at timeout
process.join(timeout=1)

# Instead check if the process terminated with
print('Process contiues to run after timeout: {}'.format(process.is_alive()))

# Or wait without a timeout
process.join()
print('Exit Code: {}'.format(process.exitcode))
