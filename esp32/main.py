import machine

# Define the GPIO pin connected to the Raspberry Pi
pin = machine.Pin(16, machine.Pin.IN)

def print_message(pin):
    print("Signal received from Raspberry Pi!")

# Attach an interrupt to the pin
pin.irq(trigger=machine.Pin.IRQ_RISING, handler=print_message)
