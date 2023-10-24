import fcntl
import time

# Define I2C constants
I2C_SLAVE = 0x0703

# Open the I2C bus
i2c = open("/dev/i2c-1", "wb", buffering=0)

# Set the I2C slave address
fcntl.ioctl(i2c, I2C_SLAVE, 0x08)

def send_to_esp32(message):
    try:
        message_bytes = [ord(c) for c in message]  # Convert message to a list of ASCII values
        i2c.write(bytes([len(message_bytes)] + message_bytes))  # Send length + data
        time.sleep(0.1)  # Add a small delay to allow ESP32 to process the data
    except Exception as e:
        print(f"Error: {e}")

# Example usage:
send_to_esp32('Hello from Raspberry Pi!')

# Close the I2C bus
i2c.close()
