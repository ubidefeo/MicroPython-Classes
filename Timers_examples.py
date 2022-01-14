from machine import Timer

timer_counter = 0

def one_shot_timer(tmr):
    print('one shot done')
    mytimer.init(period = 500, mode = Timer.PERIODIC, callback = periodic_timer)
    
def periodic_timer(tmr):
    global timer_counter
    print('tick')
    # print(tmr)
    timer_counter += 1
    print(timer_counter)
    if timer_counter >= 10:
        mytimer.deinit()
        print('timer stopped')




mytimer = Timer(-1)
mytimer.init(period = 1000, mode = Timer.ONE_SHOT, callback = one_shot_timer)
# 
