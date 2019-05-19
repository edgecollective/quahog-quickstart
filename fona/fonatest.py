from machine import UART
import time
import ssd1306
from machine import I2C
from machine import Pin
import gc

baudrate=1200
#baudrate=57600

uart = UART(1, baudrate=baudrate,rx=34,tx=13,timeout=10)

index=0

# set up the display
# i2c == (scl,sda)

i2c = I2C(-1, Pin(14), Pin(2))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

header_text="-- DEMO @ EPA --"

pin_num=23

wdi=Pin(pin_num,Pin.OUT)

# reset

wdi.value(True)
wdi.value(False)
wdi.value(True)

time.sleep(4)

while True:
   
    print('\nread:')

    while (uart.any()>0):
        a=uart.readline()
        print(a)

    time.sleep(1) 
    
    print('\nwrite')
    
    uart.write('AT+CREG?\r\n')
    
    time.sleep(1)
