import audio, time
from machine import Timer
from ulab import numpy as np

CHANNELS = 1
SIZE = 256//(2*CHANNELS)

raw_buf = None
audio.init(channels=CHANNELS, frequency=16000, gain_db=80)
show_level = Timer(-1)

def audio_callback(buf):
    # NOTE: do Not call any function that allocates memory.
    global raw_buf
    if (raw_buf == None):
        raw_buf = buf

def audio_level_cb(timer):
    print(l_lvl)

show_level.init(mode = Timer.PERIODIC, period = 200, callback = audio_level_cb)

# Start audio streaming
audio.start_streaming(audio_callback)

while (True):
    if (raw_buf != None):
        pcm_buf = np.frombuffer(raw_buf, dtype=np.int16)
        raw_buf = None

        if CHANNELS == 1:
            l_lvl = int((np.mean(abs(pcm_buf[1::2])) / 32768)*100)
        else:
            l_lvl = int((np.mean(abs(pcm_buf[1::2])) / 32768)*100)
            r_lvl = int((np.mean(abs(pcm_buf[0::2])) / 32768)*100)


# Stop streaming
audio.stop_streaming()