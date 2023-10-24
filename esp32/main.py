import machine

# Define the GPIO pin connected to the Raspberry Pi for button 1
pin_button1 = machine.Pin(16, machine.Pin.IN)

# Define the GPIO pin connected to the Raspberry Pi for button 2
pin_button2 = machine.Pin(17, machine.Pin.IN)


while True:
    def print_message(pin):
        if pin == pin_button1:
            print("Signal received from Button 1!")
        elif pin == pin_button2:
            print("Signal received from Button 2!")

    # Attach interrupts to the pins
    pin_button1.irq(trigger=machine.Pin.IRQ_RISING, handler=lambda pin: print_message(pin_button1))
    pin_button2.irq(trigger=machine.Pin.IRQ_RISING, handler=lambda pin: print_message(pin_button2))


