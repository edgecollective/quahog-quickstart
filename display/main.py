from machine import Pin
from machine import SPI

#from upy_rfm9x import RFM9x

import ssd1306
from machine import I2C

import time

i2c = I2C(-1, Pin(14), Pin(2))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
oled.fill(0)
oled.text("Starting up ...",0,0)
oled.show()

oled.pixel(0,0,1)
time.sleep(4)
oled.text("... oh, yeah.",0,50)
oled.show()


