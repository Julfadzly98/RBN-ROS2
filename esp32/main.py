from machine import Pin
from time import sleep

# Define motor control pins
motorA_input1 = Pin(5, Pin.OUT)  # Replace X with the GPIO pin number
motorA_input2 = Pin(4, Pin.OUT)  # Replace Y with the GPIO pin number
motorB_input1 = Pin(19, Pin.OUT)  # Replace Z with the GPIO pin number
motorB_input2 = Pin(18, Pin.OUT)  # Replace W with the GPIO pin number

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

connect()

def move_forward():
    motorA_input1.on()
    motorA_input2.off()
    motorB_input1.on()
    motorB_input2.off()

def move_backward():
    motorA_input1.off()
    motorA_input2.on()
    motorB_input1.off()
    motorB_input2.on()

def stop_motors():
    motorA_input1.off()
    motorA_input2.off()
    motorB_input1.off()
    motorB_input2.off()

def web_control(point):
    if point == "point_a":
        move_forward()
    elif point == "point_b":
        move_backward()
    else:
        stop_motors()

while True:
    data = input("Enter 'point_a' to move forward, 'point_b' to move backward, or 'stop' to stop motors: ")
    if data == "point_a" or data == "point_b":
        web_control(data)
    elif data == "stop":
        stop_motors()
    else:
        print("Invalid input. Please enter 'point_a', 'point_b', or 'stop'.")

