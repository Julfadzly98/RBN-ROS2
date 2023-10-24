import serial
import time

ser = serial.Serial('/dev/serial0', 9600)  # Open the serial port

def send_to_esp32(message):
    try:
        ser.write(message.encode())  # Send the message over serial
        time.sleep(0.1)  # Add a small delay to allow ESP32 to process the data
    except Exception as e:
        print(f"Error: {e}")

# Example usage:
send_to_esp32('Hello from Raspberry Pi!')
