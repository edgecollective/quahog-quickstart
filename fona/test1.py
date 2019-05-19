from machine import UART
import time
import ssd1306
from machine import I2C
from machine import Pin
import gc
import bme280
import ujson as json
import urequests as requests

pin_num=18

wdi=Pin(pin_num,Pin.OUT)


i2c = I2C(-1, Pin(14), Pin(2))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
bme=bme280.BME280(i2c=i2c)


while True:
            
    wdi.value(True)

    oled.fill(0)
    oled.text(str(pin_num)+' on',0,0)
    oled.show()

    time.sleep(3)

    wdi.value(False)                
    oled.fill(0)
    oled.text(str(pin_num)+' off',0,0)
    oled.show()

    time.sleep(3)
