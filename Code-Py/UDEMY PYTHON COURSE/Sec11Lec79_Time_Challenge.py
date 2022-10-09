import time
print("monotonic():\t", time.get_clock_info('monotonic'))
print(time.get_clock_info('perf_counter'))
print(time.get_clock_info('time'))
time.get_clock_info('process_time')
##
##print(time.time())
##help(time.time())
##print(time.perf_counter())
##print(time.monotonic())
##print(time.process_time())
