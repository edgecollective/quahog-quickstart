import ujson as json
import urequests as requests
import time
import dht
import machine
from machine import Pin
from machine import SPI

# set up the DHT22 temp + humidity sensor
d = dht.DHT22(machine.Pin(18))

# set up FARMOS params
public_key='[PUBLIC KEY]'
private_key='[PRIVATE KEY]'

# set up WIFI parameters
WIFI_NET = '[ESSID]'
WIFI_PASSWORD = '[PASSWORD]'

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

index=0

# main loop
while True:

    print ("iteration #"+str(index)+":")
    
    # make measurements from DHT22
    d.measure()
    t=d.temperature()
    h=d.humidity()

    # form the payload
    payload ={"temp": t,"humidity":h}
    print(payload)

    # connect to network
    do_connect()

    # post the data
    post_data()

    print("Posted!\n")

    index+=1

    time.sleep(5)

