from flask import Flask, render_template, request
import RPi.GPIO as GPIO 
import requests

app = Flask(__name__)

# Set up GPIO on Raspberry Pi
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)  # Assuming you're using GPIO17 as output

# Define a function to send signal to ESP32
def send_signal():
    GPIO.output(17, GPIO.HIGH)  # Send HIGH signal
    GPIO.output(17, GPIO.LOW)   # Reset to LOW

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/button_clicked', methods=['POST'])
def button_clicked():
    send_signal()
    return "Signal sent to ESP32!"

if __name__ == '__main__':
    app.run(debug=True)
