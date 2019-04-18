from machine import UART
import time
import ssd1306
from machine import I2C
from machine import Pin
import gc
import bme280
import ujson as json
import urequests as requests

sec_interval=90

# set up FARMOS params
public_key='9e854cf677302c41e069d21010d446af'
private_key='f252a12a10446aa5aca878bbee50af22'

# set up WIFI parameters
WIFI_NET = 'Artisan\'s Asylum'
WIFI_PASSWORD = 'learn.make.teach'

base_url='https://wolfesneck.farmos.net/farm/sensor/listener/'
url = base_url+public_key+'?private_key='+private_key
headers = {'Content-type':'application/json', 'Accept':'application/json'}

# function for posting data
def post_data():
    try:
    	r = requests.post(url,data=json.dumps(payload),headers=headers)
    except Exception as e:
	print(e)
	#r.close()
	return "timeout"
    else:
	r.close()
	print('Status', r.status_code)
   	return "posted"

# function for connecting to wifi
def do_connect():
    import network
    sta_if = network.WLAN(network.STA_IF)	
    if not sta_if.isconnected():
        print('connecting to network...')
	sta_if.active(False)
        sta_if.active(True)
        sta_if.connect(WIFI_NET, WIFI_PASSWORD)
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())
    
    
baudrate=1200
#baudrate=57600

y_start=0

uart = UART(1, baudrate=baudrate,rx=19,tx=21,timeout=10)

index=0
g=10 # m/s^2
rho=997 # kg/m^3

# set up the display
# i2c == (scl,sda)

i2c = I2C(-1, Pin(14), Pin(2))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
bme=bme280.BME280(i2c=i2c)


led=Pin(18,Pin.OUT)

#header_text="-- DEMO @ EPA --"

old_time=time.time()

while True:
    
    
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
            
            
            oled.text("tp: "+str(tp)+" C",0,30)
            oled.text("pp: "+str(pp)+ " mbar",0,40)
            delta_p_pa=(pp-pa)*100
            depth_m=delta_p_pa/(rho*g)
            
            
            depth_string="dp: %.2f m" % depth_m
            oled.text(depth_string,0,50)
            oled.show()
            if (depth_m>0.):
                print(depth_m)
            
            
            current_time=time.time()
            
            time_diff=current_time-old_time
            
            print(time_diff)
            
            if ((time_diff> sec_interval) or (index==0) ):
                index=index+1
                old_time=current_time
                print('post!')
                payload ={"ta": ta,"pa":pa,"ha":ha,"tp":tp,"pp":pp,"dp":depth_m}
                print(payload)
                
                # connect to network
                do_connect()

                # post the data
                post_data()                 
            
        
        except Exception as e:
            print(e)
        led.value(False)
            
            
    #time.sleep(2)
        
