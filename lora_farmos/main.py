import ujson as json
import urequests as requests
import time
import gc
import machine
from machine import Pin
from machine import SPI
from upy_rfm9x import RFM9x
import ssd1306
from machine import I2C

TIMEOUT = 1.
DISPLAY = True
OLED_LINESKIP=18
OLED_CURRENTLINE=0

feet_per_meter=3.28084

# set up the display
i2c = I2C(-1, Pin(14), Pin(2))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

# set up the 'done' pin
done_pin=Pin(22,Pin.OUT)
done_pin.value(0)

# indicate that we're starting up
oled.fill(0)
oled.text("Starting up ...",0,0)
oled.show()


# radio test
sck=Pin(25)
mosi=Pin(33)
miso=Pin(32)
cs = Pin(26, Pin.OUT)
#reset=Pin(13)
led = Pin(13,Pin.OUT)

resetNum=27

spi=SPI(1,baudrate=5000000,sck=sck,mosi=mosi,miso=miso)

rfm9x = RFM9x(spi, cs, resetNum, 915.0)


# set up FARMOS params
base_url='https://wolfesneck.farmos.net/farm/sensor/listener/'
public_key='[PUBLICKEY]'
private_key='[PRIVATEKEY]'
url = base_url+public_key+'?private_key='+private_key
headers = {'Content-type':'application/json', 'Accept':'application/json'}

# wifi parameters
#WIFI_NET = 'Artisan\'s Asylum'
#WIFI_PASSWORD = 'I won\'t download stuff that will get us in legal trouble.'

WIFI_NET = 'MOSSPIG-iPhone'
WIFI_PASSWORD = 'saladpunk'

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

index=0

# main loop
while True:
    rfm9x.receive(timeout=TIMEOUT)
    if rfm9x.packet is not None:
        try:
            packet_text = str(rfm9x.packet, 'ascii')
            rssi=str(rfm9x.rssi)
            oled.fill(0)
            #oled.text("<--",0,0)
            #oled.text(packet_text,0,30)
            oled.text("---- STUMPY ----",0,0)
            oled.text(" radio:"+rssi,0,10)
            oled.show() 
            print('Received: {}'.format(packet_text))
            print("RSSI: {}".format(rssi))
            
            s=packet_text.split(',')
            depth_meters=float(s[0])/10000.
            depth_feet=depth_meters*feet_per_meter;
            
            oled.text("  feet:"+str(depth_feet),0,20)
            oled.text("meters:"+str(depth_meters),0,30)
         
            
            fix=int(s[1])
            oled.text("gpsFix:"+str(fix),0,40)
            
            if (fix):
                lat=float(s[2])/10000.
                lon=float(s[3])/10000.
                oled.text("   lat:"+str(lat),0,50)
                oled.text("   lon:"+str(lat),0,50)
            
            oled.show() 
      
            
        except:
	        print("some error?")
	        display_text = "[{}]: (garbled msg)".format(i)
	        update_display(display_text)
	        
	        
    gc.collect()
    
