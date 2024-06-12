import _heapq
# import heapq :having problems here but working in IDLE

# heapq : the smaller the number the higher the priority
# and the bigger the number the lower the priority


# h = [10, 20, 50, 40, 60, 30, 70]
h = []

_heapq.heappush(h,20)
_heapq.heappush(h,50)
_heapq.heappush(h,10)
_heapq.heappush(h,40)
_heapq.heappush(h,60)
_heapq.heappush(h,30)
_heapq.heappush(h,70)

print(h)

_heapq.heappop(h)
print(h)
_heapq.heappop(h)
print(h)
_heapq.heappop(h)
print(h)
_heapq.heappop(h)
print(h)

h2 = [50, 20, 30, 40, 60, 10, 70]

_heapq.heapify(h2)

print(h2)

