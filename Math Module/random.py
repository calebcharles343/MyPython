'''
#IDLE

import random
random.random()
random.uniform(1,10)
random.randint(1,10)
random.randint(1,10,2) # with steps
random.randrange(1,10,2) # with steps
random.seed(10) # starting point of random numbers
random.choice(list of options) # [1,3,5,7,9,11,13]
random.choices(list of options) # [1,3,5,7,9,11,13] returns 2 random elements
random.sample(list) # similar to choices
random.shuffle(list) # rearranges elements position in list

startpoint = random.getstate() # saves the starting point of random numbers
        range of random numbers
random.getstate(startpoint) # sets startpoint

random.getrandbits(3) # 2 power 3 i.e. (2*2*2) = 8 random no is [0,1,2,3,4,5,6,7] only
'''