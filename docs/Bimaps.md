To use images on displays such as TFT or OLED, they must be loaded into the microcontroller RAM.
Although there are ways to dynamically load PNG files, I have not tested any of them.

In my classes we use monochrome OLED displays, and the tool used to encode images into `framebuf.FrameBuffer` objects containing `ByteArray` is [Lucky Resistor's MicroPython Bitmap Tool](https://luckyresistor.me/applications/micropython-bitmap-tool/) (MBT)

There are multiple ways to encode bitmaps into these objects, this is one of them.

Create grayscale images using your favourite tool.
Import these images into MBT and choose a format between
* VLSB
* HMSB
* HLSB

For the following image (courtesy of R. Sala and A. Landi) is a grayscale PNG for a projects' student

![Button](assets/story_1_1.png)

The exported `.py` file will look something like this

```Python
fb = framebuf.FrameBuffer(bytearray(
    b'\x00\x00\x00\x80\xc0\xe0\x30\x38\x18\x0c\x0c\x04\x06\x06\x06\x06\x06\x06\x06\x06\x06\x06\x06\x06\x06\x06\x06\x06\x06\x06\x06\x06'

# MORE LINES LIKE THE ONES ABOVE AND BELOW
# ...
    
    b'\x60\x60\x60\x60\x60\x60\x60\x60\x60\x60\x60\x60\x60\x60\x60\x60\x60\x60\x60\x60\x20\x30\x30\x18\x1c\x0c\x07\x03\x01\x00\x00\x00'),
    128, 64, framebuf.MONO_VLSB)

```