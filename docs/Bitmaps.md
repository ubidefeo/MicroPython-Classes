To use images on displays such as TFT or OLED, they must be loaded into the microcontroller RAM.
Although there are ways to dynamically load PNG files, I have not tested any of them.

In my classes we use Grove monochrome OLED displays based on SH1107 controllers, and the tool used to encode images into `framebuf.FrameBuffer` objects containing `ByteArray` is [Lucky Resistor's MicroPython Bitmap Tool](https://luckyresistor.me/applications/micropython-bitmap-tool/) (MBT)

There are multiple ways to encode bitmaps into these objects, this is one of them.

Create grayscale images using your favourite tool.
Import these images into MBT and choose a format between
* VLSB
* HMSB
* HLSB

The following image is a grayscale PNG for a students' projects, courtesy of R. Sala and A. Landi

![Button](assets/story_1_1.png)

The exported `story_1_1.py` file will look something like this

```Python
fb = framebuf.FrameBuffer(bytearray(
    b'\x00\x00\x00\x80\xc0\xe0\x30\x38\x18\x0c\x0c\x04\x06\x06\x06\x06\x06\x06\x06\x06\x06\x06\x06\x06\x06\x06\x06\x06\x06\x06\x06\x06'

# MORE LINES LIKE THE ONES ABOVE AND BELOW
# ...
    
    b'\x60\x60\x60\x60\x60\x60\x60\x60\x60\x60\x60\x60\x60\x60\x60\x60\x60\x60\x60\x60\x20\x30\x30\x18\x1c\x0c\x07\x03\x01\x00\x00\x00'),
    128, 64, framebuf.MONO_VLSB)

```

The code above defines a FrameBuffer object containing a `bytearray` of size _width x height_, and it can be pasted inside your `.py` code or loaded from an external `.py` file.
In order for the second option not to generate an error, this line needs to be added at the beginning

```Python
import framebuf
```

To use the image in another MicroPython program, we can simply add it to our code

```Python
from story_1_1 import fb as button_yes
```

From this point on we can use `button_yes` as graphic element to be painted on our screens 

```Python
from SH1107 import SH1107_I2C
from machine import I2C

from story_1_1 import fb as button_yes

i2c_bus = I2C(0)
display = SH1107_I2C(i2c_bus)

# vertically center on a 128x128 pixels display
display.blit(button_yes, 0, 32) 
display.show()

```

Done.