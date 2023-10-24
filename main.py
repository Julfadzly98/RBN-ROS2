import serial
import time
from flask import Flask, render_template

ser = serial.Serial('/dev/serial0', 9600)  # Open the serial port

app = Flask(__name__)

def send_to_esp32(message):
    try:
        ser.write(message.encode())  # Send the message over serial
        time.sleep(0.1)  # Add a small delay to allow ESP32 to process the data
    except Exception as e:
        print(f"Error: {e}")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/button1')
def button1():
    send_to_esp32('Button 1 pressed!')
    return 'Button 1 pressed!'

@app.route('/button2')
def button2():
    send_to_esp32('Button 2 pressed!')
    return 'Button 2 pressed!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
