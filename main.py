import smbus
import time

# Create an I2C object
bus = smbus.SMBus(1)  # 1 indicates /dev/i2c-1, for Raspberry Pi 2/3/4. Use 0 for Raspberry Pi 1.

def send_to_esp32(message):
    try:
        # Convert message to a list of ASCII values
        message_bytes = [ord(c) for c in message]
        # Send data to the ESP32
        bus.write_i2c_block_data(0x08, 0, message_bytes)  # 0x08 is the ESP32 I2C address
        time.sleep(0.1)  # Add a small delay to allow ESP32 to process the data
    except Exception as e:
        print(f"Error: {e}")

# Example usage:
send_to_esp32('Hello from Raspberry Pi!')
