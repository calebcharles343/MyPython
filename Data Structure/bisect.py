# bisect : maintains a list in a sorted order

# import bisect : having problems here but working in IDLE

'''

l = [10, 20, 20, 40, 50, 60, 70, 90]

bisect.insort(l, 25)
print(l)  # result: [10, 20, 20, 25, 40, 50, 60, 70, 90]
bisect.insort_left(l, 90)
print(l)  # result: [10, 20, 20, 25, 40, 50, 60, 70, 90, 90]

print(bisect.bisect(l,5))  # result: 0 -> i.e. position index where the new element would be placed

print(bisect.bisect_left(l,20))  # result: 1
print(bisect.bisect_right(l,20))  # result: 3
'''
