"""
New in 3.8! Shared memory between processes!
Create SharedMemory objects that can be referenced by a string name.
"""

import multiprocessing
from multiprocessing import shared_memory


def process_1():
    sm = shared_memory.SharedMemory(name='my_shared_memory')
    sm.buf[:6] = bytearray('Hello ', encoding='ascii')


def process_2():
    sm = shared_memory.SharedMemory(name='my_shared_memory')
    sm.buf[6:12] = bytearray('World!', encoding='ascii')


sm = shared_memory.SharedMemory(create=True, size=12, name='my_shared_memory')
print('Created SharedMemory:', sm)
print('SharedMemory name:', sm.name)
print('buffer:', sm.buf)
print('buffer content:', [x for x in sm.buf])

# Define our processes
process1 = multiprocessing.Process(target=process_1)
process2 = multiprocessing.Process(target=process_2)

# Start the processes
process1.start()
process2.start()

# Wait for processes to finish
process1.join()
process2.join()

print('Final Output')
print([chr(x) for x in sm.buf])


# Clean up
sm.close()
sm.unlink()
