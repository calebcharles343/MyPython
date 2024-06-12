# Mutex

from threading import *
from time import *


def display(str1):
    l.acquire()
    for x in str1:
        print(x)
        sleep(0.3)
    l.release()


l = Lock() # To avoid race condition
ti = Thread(target=display, args=('HELLO WORLD ',))
t2 = Thread(target=display, args=('you are welcome',))

ti.start()
t2.start()

ti.join()
t2.join()
