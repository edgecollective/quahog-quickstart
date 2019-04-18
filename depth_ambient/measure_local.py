from machine import UART
import time
import ssd1306
from machine import I2C
from machine import Pin
import gc
import bme280

baudrate=1200
#baudrate=57600

y_start=0

uart = UART(1, baudrate=baudrate,rx=19,tx=21,timeout=10)

index=-1
g=10 # m/s^2
rho=997 # kg/m^3

# set up the display
# i2c == (scl,sda)

i2c = I2C(-1, Pin(14), Pin(2))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
bme=bme280.BME280(i2c=i2c)


led=Pin(18,Pin.OUT)

#header_text="-- DEMO @ EPA --"
while True:
    
    index=index+1
    
    
    a=uart.readline()
    if (a!=None):
        #print(a)
        led.value(True)
        try:
        
        
            bme280_params=bme.values
            #print(bme280_params)
            ta=float(bme280_params[0])
            pa=float(bme280_params[1])
            ha=float(bme280_params[2])
            
            oled.fill(0)
            oled.text("ta: "+str(ta)+" C",0,0)
            oled.text("pa: "+str(pa)+" mbar",0,10)
            
            ha_string="ha: %.2f" % ha
            oled.text(ha_string,0,20)
            
            packet_text = str(a, 'ascii')
            #print(packet_text)
            params=packet_text.strip().split(',')
            #print(params)
            
            tp=float(params[0])
            pp=float(params[1])
            
            index=index+1
            
            oled.text("tp: "+str(tp)+" C",0,30)
            oled.text("pp: "+str(pp)+ " mbar",0,40)
            delta_p_pa=(pp-pa)*100
            depth_m=delta_p_pa/(rho*g)
            
            
            depth_string="dp: %.2f m" % depth_m
            oled.text(depth_string,0,50)
            oled.show()
            if (depth_m>0.):
                print(depth_m)  
        
        except Exception as e:
            print(e)
        led.value(False)
            
            
    #time.sleep(2)
        
