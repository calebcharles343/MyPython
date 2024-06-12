import time
import datetime
'''
Time module: in Python provides various time-related functions. 
Here are some key points:

1. **Epoch and Seconds Since the Epoch**:
   - The epoch is the starting point for time calculations 
   (January 1, 1970, 00:00:00 UTC).
   
   - "Seconds since the epoch" refers to the total elapsed 
   seconds since the epoch (excluding leap seconds).

2. **Common Functions**:
   - `time()`: Returns the current time in seconds since 
   the epoch.
   
   - `gmtime()`: Converts seconds since the epoch to a 
   struct_time in UTC.
   
   - `localtime()`: Converts seconds since the epoch to 
   a struct_time in local time.
   
   - `strftime()`: Formats a struct_time into a string 
   representation.
   
   - `strptime()`: Parses a string into a struct_time.

3. **Struct Time**:
   - A struct_time represents time as a sequence of 9 integers 
   (year, month, day, hour, minute, second, etc.).
   - It also offers attribute names for individual fields.

4. **Precision and Sleep**:
   - `sleep(seconds)`: Suspends execution for the specified 
   duration.
   - Precision varies across platforms (e.g., 
   Unix ticks 50-100 times per second).

Remember to consult the [official Python documentation]
(https://docs.python.org/3/library/time.html) 
for detailed information and examples. 

'''

print('Time:', time.time())
print('GMTime:', time.gmtime())
print('LocalTime:', time.localtime())
# print('Strytime', time.strftime())
# print('Strptime', time.strptime())
print('########################################')

lt = time.localtime()
print(type(lt))
print(lt.tm_year)
print(lt.tm_mon)
print(lt.tm_mday)
print(lt.tm_hour)
print(lt.tm_min)
print(lt.tm_sec)

print('############# TIME EXPRESSION #################')
lt = time.localtime(time.time()/2)
print(lt.tm_year)

print('########################################')

print('Current time:', time.ctime())
print('Static Method:', datetime.datetime.now())
print('Static Method:', datetime.datetime.today())