import machine, neopixel
PIXEL_PIN   = machine.Pin(15, machine.Pin.OUT)
np = neopixel.NeoPixel(PIXEL_PIN, 16)
np.fill((255, 0, 255))
np.write()
print('hello micropython')
