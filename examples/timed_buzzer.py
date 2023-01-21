from machine import Timer, Pin

buzzer = Pin(6, Pin.OUT)

buzzer_timeout = Timer(-1)
buzzer_timer = Timer(-1)

buzzer_time_on = 500
buzzer_time_delay = 500

def buzzer_on(timer):
    buzzer.on()
    buzzer_timeout.init(mode = Timer.ONE_SHOT, period = buzzer_time_on, callback = buzzer_off)

def buzzer_off(timer):
    buzzer.off()
    
def start_buzzing(on, off):
    global buzzer_time_on, buzzer_time_off
    buzzer_time_on = on
    buzzer_time_off = off
    buzzer_timer.deinit()
    buzzer_timer.init(mode = Timer.PERIODIC, period = buzzer_time_on + buzzer_time_delay, callback = buzzer_on)
