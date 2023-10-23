import network

def connect():
    import network
 
    ssid = "smartspacekk" 
    password = "smartspace09" 
 
    station = network.WLAN(network.STA_IF)
 
    if station.isconnected() == True:
        print("Already connected")
        return
 
    station.active(True)
    station.connect(ssid, password)
 
    while station.isconnected() == False:
        pass
 
    print("Connection successful")
    print(station.ifconfig())

wlan = network.WLAN(network.STA_IF)
print(wlan.ifconfig())
