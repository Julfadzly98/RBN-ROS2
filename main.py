from flask import Flask, render_template, request
import RPi.GPIO as GPIO
import requests

app = Flask(__name__)

# Set up GPIO on Raspberry Pi
GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)  # Assuming you're using GPIO17 as output
GPIO.setmode(GPIO.BCM)
GPIO.setup(15, GPIO.OUT)

# Define a function to send signal to ESP32
def send_signal():
    GPIO.output(14, GPIO.HIGH)  # Send HIGH signal
    GPIO.output(14, GPIO.LOW)   # Reset to LOW

def send_signals():
    GPIO.output(15, GPIO.HIGH)  # Send HIGH signal
    GPIO.output(15, GPIO.LOW)   # Reset to LOW

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/button_clicked', methods=['POST'])
def button_clicked():
    send_signal()
    return "Button 1"

@app.route('/button_clickeds', methods=['POST'])
def button_clickeds():
    send_signals()
    return "Button 2"

if __name__ == '__main__':
    app.run(debug=True)
