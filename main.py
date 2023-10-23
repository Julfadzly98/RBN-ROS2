from flask import Flask, render_template
import serial

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<action>')
def control(action):
    if action == "point_a":
        ser.write(b'1')
    elif action == "point_b":
        ser.write(b'2')
    return render_template('index.html')

if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyS0', baudrate=115200)  # Assuming ESP32 is connected to UART0
    app.run(debug=True, host='0.0.0.0')
