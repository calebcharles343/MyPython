from threading import *
from time import *


class MyData:
    def __init__(self):
        self.data = 0
        self.conditionVariable = Condition()  # works as flag() and lock()

    def put(self, d):
        self.conditionVariable.acquire()  # acquire lock :
        self.conditionVariable.wait(timeout=0)
        self.data = d
        self.conditionVariable.notify()  # notifies consumer
        self.conditionVariable.release()
        sleep(0.5)

    def get(self):
        self.conditionVariable.acquire()
        self.conditionVariable.wait(timeout=0)
        x = self.data
        self.conditionVariable.notify()
        self.conditionVariable.release()
        sleep(0.5)
        return x


def producer(data):
    i = 1
    while True:
        data.put(i)
        print('Producer:', i)
        i += 1


def consumer(data):
    while True:
        x = data.get()
        print('Consumer:', x)


data = MyData()
t1 = Thread(target=lambda: producer(data))
t2 = Thread(target=lambda: consumer(data))

t1.start()
t2.start()

t1.join()  # join with main method
t2.join()  # join with main method
