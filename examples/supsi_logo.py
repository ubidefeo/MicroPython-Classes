import framebuf

logo = framebuf.FrameBuffer(bytearray(
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    b'\x00\x00\x00\x00\xe0\xf8\xfc\xfc\xfe\xfe\x3f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x3f\x3e\x3e\x0e\x00\x00\x00\x00\x00\x00\x00\xff\xff'
    b'\xff\xff\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\xff\x00\x00\x00\x00\x00\x00\x00'
    b'\xff\xff\xff\xff\xff\xff\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x3f\x3e\xfe\xfe\xfc\xfc\xf8\xf0\xc0\x00\x00\x00\x00\xf0\xf8\xfc'
    b'\xfe\xfe\x7f\x3f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x3f\x3e\x3e\x06\x00\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\xff\x00\x00\x00'
    b'\x00\x00\x00\x00\x0f\x1f\x7f\x7f\xff\xff\xfc\xf8\xf0\xf0\xe0\xe0\xc0\xc0\x80\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xff'
    b'\xff\xff\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\xff\x00\x00\x00\x00\x00\x00\x00'
    b'\xff\xff\xff\xff\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\xc0\xff\xff\xff\xff\xff\xff\x00\x00\x00\x00\x0f\x3f\x7f'
    b'\xff\xff\xfe\xfc\xf8\xf0\xf0\xe0\xe0\xc0\xc0\x80\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\xff\x00\x00\x00'
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x03\x03\x07\x07\x0f\x0f\x1f\x3f\xff\xff\xfe\xfe\xf8\xf0\x00\x00\x00\x00\x00\xff\xff'
    b'\xff\xff\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc0\xff\xff\xff\xff\xff\x00\x00\x00\x00\x00\x00\x00'
    b'\xff\xff\xff\xff\xff\xff\x00\x00\x00\x00\x3e\x3e\x3e\x3e\x3e\x3e\x3f\x1f\x1f\x1f\x0f\x07\x03\x01\x00\x00\x00\x00\x00\x00\x00\x00'
    b'\x00\x00\x01\x01\x03\x03\x07\x07\x0f\x0f\x1f\x3f\xff\xff\xfe\xfc\xf8\xe0\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\xff\x00\x00\x00'
    b'\x00\x00\x00\x40\xf8\xf8\xf8\xf8\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf8\xf8\xfc\xff\xff\x7f\x3f\x1f\x07\x00\x00\x00\x00\x00\x01\x07'
    b'\x1f\x3f\x7f\x7f\xff\xfc\xf8\xf8\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf8\xfc\xfe\x7f\x7f\x3f\x1f\x0f\x03\x00\x00\x00\x00\x00\x00\x00'
    b'\xff\xff\xff\xff\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x60\xfc\xf8\xf8'
    b'\xf8\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf8\xf8\xfc\xff\x7f\x7f\x3f\x1f\x03\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\xff\x00\x00\x00'
    b'\x00\x00\x00\x00\x00\x00\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    b'\x00\x00\x00\x00\x00\x00\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    b'\x01\x01\x01\x01\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01'
    b'\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x01\x01\x01\x00\x00\x00'
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
    128, 56, framebuf.MONO_VLSB)