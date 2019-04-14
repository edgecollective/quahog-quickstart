from machine import UART
import time

baudrate=1200
#baudrate=57600

uart = UART(1, baudrate=baudrate,rx=19,tx=21,timeout=10)

while True:
    a=uart.readline()
    if (a!=None):
        print(a)
        try:
            packet_text = str(a, 'ascii')
            print(packet_text)
            params=packet_text.strip().split(',')
            print(params)
        except Exception as e:
            print(e)
