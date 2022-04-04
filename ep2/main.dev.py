from machine import Pin, Timer
from time import sleep

led = Pin(28, Pin.OUT)
ledTimer = Timer(-1)

ledTimer.init(period=50, mode=Timer.PERIODIC, callback=lambda t:led.toggle())
