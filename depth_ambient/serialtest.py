from machine import UART
import time
import ssd1306
from machine import I2C
from machine import Pin
import gc

baudrate=1200
#baudrate=57600

uart = UART(1, baudrate=baudrate,rx=19,tx=21,timeout=10)

index=0

# set up the display
# i2c == (scl,sda)

i2c = I2C(-1, Pin(14), Pin(2))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

header_text="-- DEMO @ EPA --"
while True:
    a=uart.readline()
    if (a!=None):
        print(a)
        try:
            packet_text = str(a, 'ascii')
            print(packet_text)
            params=packet_text.strip().split(',')
            print(params)
            
            temp=params[0]
            press=params[1]
            depth=params[2]
            
            index=index+1
            
            oled.fill(0)
            oled.text(header_text,0,0)
            oled.text("reading #"+str(index),0,20)
            oled.text("t: "+str(params[0]+" C"),0,35)
            oled.text("p: "+str(params[1]+ " mbar"),0,45)
            oled.text("d: "+str(params[2])+ " meters",0,55)
            oled.show()
            
            
        except Exception as e:
            print(e)
