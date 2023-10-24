import smbus

# Create an I2C object
bus = smbus.SMBus(1)  # 1 indicates /dev/i2c-1, for Raspberry Pi 2/3/4. Use 0 for Raspberry Pi 1.

def send_to_esp32(message):
    bus.write_i2c_block_data(0x8, 0, [ord(c) for c in message])  # 0x8 is the ESP32 I2C address

# Example usage:
send_to_esp32('Hello from Raspberry Pi!')
