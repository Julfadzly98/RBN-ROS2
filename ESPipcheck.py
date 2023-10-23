import network

wlan = network.WLAN(network.STA_IF)
print(wlan.ifconfig())
