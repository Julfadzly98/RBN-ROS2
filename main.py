from machine import Pin, I2C

i2c = I2C(-1, scl=Pin(22), sda=Pin(21))  # Create I2C object

def receive_from_raspberry_pi():
    if i2c.any():
        return i2c.read()
    else:
        return None

# Example usage:
while True:
    received_message = receive_from_raspberry_pi()
    if received_message:
        print(received_message.decode('utf-8'))

