import machine

# Define the GPIO pin connected to the Raspberry Pi
pin = machine.Pin(2, machine.Pin.IN)
pins = machine.Pin(4, machine.Pin.IN)


while True:
    
    def print_message(pin):
        print("Button 1 Received")

    # Attach an interrupt to the pin
    pin.irq(trigger=machine.Pin.IRQ_RISING, handler=print_message)
    
    def print_messages(pins):
        print("Button 2 Received")

    # Attach an interrupt to the pin
    pins.irq(trigger=machine.Pin.IRQ_RISING, handler=print_messages)

