import serial
import time

# Set up the serial connection
ser = serial.Serial('/dev/serial0', 115200, timeout=1)  # Change the port if necessary

def send_to_esp32(message):
    ser.write(message.encode('utf-8'))

# Example usage:
send_to_esp32('Hello from Raspberry Pi!')
