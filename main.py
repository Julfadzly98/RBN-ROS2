import serial

ser = serial.Serial('/dev/serial0', 9600)  # Open the serial port

def send_to_esp32(message):
    try:
        ser.write(message.encode())  # Send the message over serial
    except Exception as e:
        print(f"Error: {e}")

# Example usage:
send_to_esp32('Hello from Raspberry Pi!')
