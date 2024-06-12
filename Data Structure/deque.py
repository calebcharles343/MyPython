from collections import deque
'''
Deque: double ended queue means operations can be performed
from both ends of the queue as both Queue and Stack
- Queue: elements are inserted and deleted in first-in, first-out
(FIFO) fashion OR elements are inserted from the right side and deleted
from the left side.
- Stack: elements are inserted and deleted in last-in, first-out
(LIFO) fashion OR elements are inserted and deleted from the right side only.
'''

l = [1,2,3,4,5]
q = deque(l)
print(q)

q.append(6)
print(q)

q.appendleft(7)
print(q)

q.popleft()
print(q)

q.extend([10, 20, 30])
print(q)

q.extendleft([0])
print(q)

# q.rotate()
q.rotate(2)
print(q)