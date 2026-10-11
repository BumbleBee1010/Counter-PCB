# MicroPython SH1106 OLED driver, I2C and SPI interfaces
# Copyright (c) 2016-2022 Robert Hammelrath and others
# GPL V3 License
from micropython import const
import framebuf

# Register addresses
SET_CONTRAST = const(0x81)
SET_NORM_INV = const(0xA6)
SET_DISP = const(0xAE)
SET_SCAN_DIR = const(0xC0)
SET_SEG_REMAP = const(0xA0)
SET_LOW_COL = const(0x00)
SET_HIGH_COL = const(0x10)
SET_PAGE_ADDR = const(0xB0)

class SH1106(framebuf.FrameBuffer):
    def __init__(self, width, height, external_vcc):
        self.width = width
        self.height = height
        self.external_vcc = external_vcc
        self.pages = self.height // 8
        self.buffer = bytearray(self.pages * self.width)
        super().__init__(self.buffer, self.width, self.height, framebuf.MONO_VLSB)
        self.init_display()

    def init_display(self):
        for cmd in (
            SET_DISP | 0x00,  # off
            SET_LOW_COL | 0x00,  # set lower column address
            SET_HIGH_COL | 0x00,  # set higher column address
            SET_PAGE_ADDR | 0x00,  # set page address
            SET_CONTRAST, 0x7F,  # contract control
            SET_SEG_REMAP | 0x01,  # eth remap
            SET_NORM_INV | 0x00,  # normal
            0xA8, 0x3F,  # multiplex ratio
            SET_SCAN_DIR | 0x08,  # scan dir reverse
            0xD3, 0x00,  # display offset
            0xD5, 0x50,  # osc division
            0xD9, 0x22,  # pre-charge period
            0xDA, 0x12,  # com pins deviation
            0xDB, 0x35,  # vcomh ratio
            0x8D, 0x14,  # charge pump enable
            SET_DISP | 0x01,  # on
        ):
            self.write_cmd(cmd)
        self.show()

    def poweroff(self):
        self.write_cmd(SET_DISP | 0x00)

    def poweron(self):
        self.write_cmd(SET_DISP | 0x01)

    def contrast(self, contrast):
        self.write_cmd(SET_CONTRAST)
        self.write_cmd(contrast)

    def invert(self, invert):
        self.write_cmd(SET_NORM_INV | (invert & 1))

    def show(self):
        for page in range(self.pages):
            self.write_cmd(SET_PAGE_ADDR | page)
            self.write_cmd(SET_LOW_COL | 2)  # SH1106 has a 2-column offset
            self.write_cmd(SET_HIGH_COL | 0)
            self.write_data(self.buffer[page * self.width : (page + 1) * self.width])

class SH1106_I2C(SH1106):
    def __init__(self, width, height, i2c, addr=0x3C, external_vcc=False):
        self.i2c = i2c
        self.addr = addr
        self.temp = bytearray(2)
        super().__init__(width, height, external_vcc)

    def write_cmd(self, cmd):
        self.temp[0] = 0x00  # Co=0, D/C#=0
        self.temp[1] = cmd
        self.i2c.writeto(self.addr, self.temp)

    def write_data(self, buf):
        self.i2c.writeto(self.addr, b"\x40" + buf)
