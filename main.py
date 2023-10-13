from flask import Flask, render_template
import serial

app = Flask(__name__)

ser = serial.Serial('/dev/serial0', 9600) # Open communication with ESP32

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/motor/<int:motor_number>/<int:direction>')
def control_motor(motor_number, direction):
    command = f"{motor_number}{direction}\n"
    ser.write(command.encode())
    return "Motor command sent!"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
