import machine
from machine import Pin, UART
import time

# Initialize UART
uart = UART(1, baudrate=9600, tx=14, rx=13)

# Define motor pins
motor1_in1 = Pin(4, Pin.OUT)
motor1_in2 = Pin(5, Pin.OUT)
motor2_in1 = Pin(18, Pin.OUT)
motor2_in2 = Pin(19, Pin.OUT)

# Define button pins
button_a = Pin(12, Pin.IN, Pin.PULL_UP)
button_b = Pin(27, Pin.IN, Pin.PULL_UP)

def control_motor(motor, direction):
    if motor == 1:
        motor1_in1.value(direction)
        motor1_in2.value(not direction)
    elif motor == 2:
        motor2_in1.value(direction)
        motor2_in2.value(not direction)

def check_buttons():
    if not button_a.value():
        return 1, 1  # Motor 1, Forward
    elif not button_b.value():
        return 1, 0  # Motor 1, Backward
    else:
        return None, None

while True:
    motor, direction = check_buttons()
    if motor is not None:
        control_motor(motor, direction)
        time.sleep(0.1)
