# Find time taken for a code to execute
"""
import datetime
start_time = datetime.datetime.now()

for i in range(100000000 ):
    pass

end_time = datetime.datetime.now()

duration = end_time - start_time
print('Execution Time:', duration.seconds, duration.microseconds)
"""

# OR

import time
start_time = time.time()

for i in range(100000000 ):
    pass

end_time = time.time()

duration = end_time - start_time
print('Execution Time:', duration)