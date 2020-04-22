import network
from machine import Pin
def connect(ssid,password):
    sta_if = network.WLAN(network.STA_IF)
    p2 = Pin(2, Pin.OUT)
    #我们在这里把接入点接口禁用，方便观看实验效果，非实验可以去掉
    sta_if.active(False)
    if not sta_if.isconnected():
        p2.value(0)
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect(ssid,password)
        while not sta_if.isconnected():
            pass
    if sta_if.isconnected():
        print('connect success')
        p2.value(1)
        print('network config:', sta_if.ifconfig())
