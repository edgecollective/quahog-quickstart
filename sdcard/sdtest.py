import gc

from machine import Pin
from machine import SPI
#from upy_rfm9x import RFM9x
from machine import I2C
import ssd1306
import sdcard
import os

TIMEOUT = 5
DISPLAY = True
OLED_LINESKIP=18
OLED_CURRENTLINE=0


i2c = I2C(-1, Pin(14), Pin(2))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

# sd card test

sck=Pin(16)
mosi=Pin(4)
miso=Pin(17)
cs = Pin(15, Pin.OUT)
spi2=SPI(2,baudrate=5000000,sck=sck,mosi=mosi,miso=miso)

sd = sdcard.SDCard(spi2, cs)
os.mount(sd,'/sd')
output=os.listdir('/sd')
print(output)

OLED_CURRENTLINE=OLED_CURRENTLINE+OLED_LINESKIP
oled.text("Sd card works;",0,OLED_CURRENTLINE)
oled.show()


# wrap up
OLED_CURRENTLINE=OLED_CURRENTLINE+OLED_LINESKIP
oled.text("... oh, yeah.",0,OLED_CURRENTLINE)
oled.show()

