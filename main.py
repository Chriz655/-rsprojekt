from machine import Pin, I2C
import time
from vl53l0x import VL53L0X

# I2C-tilkobling for VL53L0X
i2c = I2C(0, scl=Pin(5), sda=Pin(4))

# Initialiser ToF-sensor
tof = VL53L0X(i2c)
tof.start()

# LED som indikator (koblet til GP15)
led = Pin(15 , Pin.OUT)

# Transistorstyring (koblet til GP14)
transistor = Pin(14, Pin.OUT)

# Terskel (10 cm = 100 mm)
terskel = 500

while True:
    avstand = tof.read()
    print("Avstand:", avstand, "mm")

    if avstand < terskel:
        led.value(1)        # Tenn LED
        transistor.value(1) # Aktiver transistor
    else:
        led.value(0)
        transistor.value(0)

    time.sleep(0.5)



