import machine

# Define motor control pins
motorA_input1 = machine.Pin(5, machine.Pin.OUT)  # Replace X with the GPIO pin number
motorA_input2 = machine.Pin(4, machine.Pin.OUT)  # Replace Y with the GPIO pin number
motorB_input1 = machine.Pin(19, machine.Pin.OUT)  # Replace Z with the GPIO pin number
motorB_input2 = machine.Pin(18, machine.Pin.OUT)  # Replace W with the GPIO pin number

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

# UART Configuration
uart = machine.UART(0, baudrate=115200)
uart.init(115200, bits=8, parity=None, stop=1)

while True:
    data = uart.read(1)  # Read one byte
    if data == b'1':
        move_forward()
    elif data == b'2':
        move_backward()
    else:
        stop_motors()
