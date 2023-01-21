from machine import Timer

timer_counter = 0

def one_shot_callback(timer_object):
    print('one shot done')
    periodic_timer.init(period = 500, mode = Timer.PERIODIC, callback = periodic_callback)
    
def periodic_callback(timer_object):
    global timer_counter
    print('tick')
    # print(tmr)
    timer_counter += 1
    print(timer_counter)
    if timer_counter >= 10:
        timer_object.deinit()
        print('timer stopped')



periodic_timer = Timer(-1)

# the one shot timer will start a periodic timer after 2 seconds (2000 ms)
one_shot_timer = Timer(-1)
one_shot_timer.init(period = 1000, mode = Timer.ONE_SHOT, callback = one_shot_callback)
