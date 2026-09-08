import network
import time

from config import WIFI_SSID, WIFI_PASS


def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)

    if wlan.isconnected():
        print("Already connected")
        print("IP:", wlan.ifconfig()[0])
        return wlan

    print("Connecting to Wi-Fi!")
    print("SSID:", WIFI_SSID)

    wlan.connect(WIFI_SSID, WIFI_PASS)

    for i in range(30):
        status = wlan.status()

        print("status:", status)

        if wlan.isconnected():
            break

        if status < 0:
            break

        time.sleep(1)

    if not wlan.isconnected():
        raise RuntimeError(
            "Wi-Fi connection failed. status={}".format(wlan.status())
        )

    print("Connected!")
    print("IP:", wlan.ifconfig()[0])
    print("Network:", wlan.ifconfig())

    return wlan