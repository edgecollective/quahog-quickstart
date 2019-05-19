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
public_key='ebb4OB1GGqSzL8g4bPmzUm9864wo'
private_key='2llaO9KWWwsmlXWaby2mFQPBveLD'

# set up WIFI parameters
WIFI_NET = 'Artisan\'s Asylum'
WIFI_PASSWORD = 'learn.make.teach'

base_url='http://142.93.123.71:8080/input/'
get_url = base_url+public_key+'?private_key='+private_key
headers = {'Content-type':'application/json', 'Accept':'application/json'}

led=Pin(18,Pin.OUT)

wdi=Pin(22,Pin.OUT)


def get_data(url):
    try:
    	r = requests.get(url)
        return r
    except Exception as e:
	    print(e)
    else:
	    r.close()    

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

i2c = I2C(-1, Pin(14), Pin(2))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)


oled.fill(0)
oled.text('yeah!',0,0)
oled.show()
