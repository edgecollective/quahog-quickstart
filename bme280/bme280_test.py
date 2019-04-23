import machine, _thread, time
import micropython, gc
import bme280
i2c=machine.I2C(scl=machine.Pin(14),sda=machine.Pin(2))
bme=bme280.BME280(i2c=i2c)

params=bme.values
print(params)
