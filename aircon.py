from machine import Pin

led = Pin("LED", Pin.OUT)

def power_on():
    led.value(1)
    print("Aircon on")
    
def power_off():
    led.value(0)
    print("Aircon off")
    
    