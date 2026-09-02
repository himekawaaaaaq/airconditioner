import network
import time

from config import WIFI_SSID,WIFI_PASS

def connect_wifi():
    wlan = network.WLAN(network.WLAN.IF_STA)
    wlan.active(True)
    
    if wlan.isconnected():
        return wlan
    
    print("Connecting to wi-fi!")
    
    wlan.connect(WIFI_SSID,WIFI_PASS)
    
    timeout = 15
    
    while not wlan.isconnected():
        if timeout <= 0:
            raise RuntimeError("wi-fi connection failed")
        
        print(".")
        time.sleep(1)
        timeout -= 1
        
    print("Connected")
    print("IP:",wlan.ipconfig("addr4"))
    
    return wlan