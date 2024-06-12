# Semaphore
from threading import *
from time import *


def display(str1):
    s.acquire()
    for x in str1:
        print(x)
        sleep(0.3)
    s.release()


s = Semaphore(1)  # To control race condition
ti = Thread(target=display, args=('HELLO WORLD ',))
t2 = Thread(target=display, args=('you are welcome',))
t3 = Thread(target=display, args=('0123456789',))

ti.start()
t2.start()
t3.start()

ti.join()
t2.join()
t3.join()
