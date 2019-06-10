from machine import UART
import time
from machine import Pin
import gc
import random

import ssd1306
from machine import I2C

i2c = I2C(-1, Pin(14), Pin(2))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
oled.fill(0)
oled.text("Sleeping for 10 sec ...",0,0)
oled.show()

time.sleep(10)

oled.fill(0)
oled.text("Starting post ...",0,0)
oled.show()


baudrate=9600
#baudrate=57600

# sensor data + url
url_base="http://mosspig.club/input/dVlKyQD6pehDgNjjXlNxC2rOd9d?private_key=eQd7OyXp5gInDq00QeqgCy9M2b2"

temp=round(20+random.random(),2)

url_full=url_base+"&temp="+str(temp)
print(url_full)

uart = UART(1, baudrate=baudrate,rx=19,tx=21,timeout=10)
uart.write("AT+SAPBR=0,1\r")
time.sleep(1)
print(uart.readline())
print(uart.readline())
uart.write("AT+SAPBR=3,1,\"APN\",\"fast.t-mobile.com\"\r")
time.sleep(1)
print(uart.readline())
print(uart.readline())
uart.write("AT+CREG?\r")
print(uart.readline())
print(uart.readline())
uart.write("AT+SAPBR=2,1\r")
time.sleep(1)
print(uart.readline())
print(uart.readline())
uart.write("AT+SAPBR=1,1\r")
time.sleep(1)
print(uart.readline())
print(uart.readline())
uart.write("WAIT=6\r")
print(uart.readline())
print(uart.readline())
uart.write("AT+CMGF=0\r")
time.sleep(1)
print(uart.readline())
print(uart.readline())
uart.write("AT+HTTPINIT\r")
time.sleep(1)
print(uart.readline())
print(uart.readline())
#uart.write("AT+HTTPSSL=1\r")
#time.sleep(1)
#print(uart.readline())
#print(uart.readline())
#uart.write("AT+HTTPPARA=\"URL\",\"https://enedig34tr0td.x.pipedream.net\"\r")
#uart.write("AT+HTTPPARA=\"URL\",\"https://wolfesneck.farmos.net/farm/sensor/listener/834c74e03901cd1702c0a3060803f767?private_key=bfe468dc77b5530d65319b67cc39cdbc\"\r")


#uart.write("AT+HTTPPARA=\"URL\",\""+url_full+"\"\r");
#uart.write("AT+HTTPPARA=\"URL\",\"http://142.93.123.71:8080/input/MjYYakyDzvs6amYM8qB6SPa3lAdv?private_key=Eq44LVm8BesGXlnZ3m2GFv6RBbpe&temp=3.16\"\r")

#uart.write("AT+HTTPPARA=\"URL\",\"https://en93klhmkdkf5.x.pipedream.net\"\r")
#uart.write("AT+HTTPPARA=\"URL\",\"http://mosspig.club\"\r")
uart.write("AT+HTTPPARA=\"URL\",\""+url_full+"\"\r")

time.sleep(1)
print(uart.readline())
print(uart.readline())
uart.write("AT+HTTPPARA=\"CID\",1\r")
time.sleep(1)
print(uart.readline())
print(uart.readline())
#uart.write("AT+HTTPDATA=0,1000\r")
#time.sleep(1)
#print(uart.readline())
#print(uart.readline())
uart.write("AT+HTTPACTION=0\r")
time.sleep(1)
print(uart.readline())
print(uart.readline())
uart.write("AT+HTTPREAD\r")
time.sleep(1)
a=uart.readline()
b=uart.readline()
print(a)
print(b)

oled.fill(0)
oled.text(a,0,0)
oled.show()

uart.write("WAIT=6\r")
print(uart.readline())
print(uart.readline())
uart.write("AT+HTTPTERM\r")
time.sleep(1)
print(uart.readline())
print(uart.readline())
