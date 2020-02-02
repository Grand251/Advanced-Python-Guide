"""Comparison of Lock and RLock"""

import os
import time
import threading


def locking_thread(val):
    with threading.Lock():
        time.sleep(.1)
        print(str(val) + ' 1')
        time.sleep(.1)
        print(str(val) + ' 2')
        time.sleep(.1)
        print(str(val) + ' 3')


def non_locking_thread(val):
    time.sleep(.1)
    print(str(val) + ' 1')
    time.sleep(.1)
    print(str(val) + ' 2')
    time.sleep(.1)
    print(str(val) + ' 3')

threads = []
print('Non Locking')
for val in ['a', 'b', 'c']:
    thread = threading.Thread(target=non_locking_thread, args=(val, )).start()

time.sleep(1)
# But if we want out threads to run a set of their instructions,
# we can acquire a lock as done in locking_thread()

print('Locking')
for val in ['a', 'b', 'c']:
    threading.Thread(target=locking_thread, args=(val, )).start()
