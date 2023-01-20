import time

print('starting program')

time.sleep(1)
print('I slept for 1 second: power nap!')

time.sleep_ms(500)
print('I slept for half a second: too little!')

start = time.ticks_ms()
print(f'time I\'ve been alive {start}')

time.sleep(2)


delta = time.ticks_diff(time.ticks_ms(), start)
print(f'Since start was marked it\'s been {delta} milliseconds')