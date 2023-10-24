from flask import Flask, render_template, request
import RPi.GPIO as GPIO

app = Flask(__name__)

# Set up GPIO on Raspberry Pi
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)  # Assuming you're using GPIO17 as output for the first button
GPIO.setup(18, GPIO.OUT)  # Assuming you're using GPIO18 as output for the second button

# Define a function to send signal to ESP32
def send_signal(pin):
    GPIO.output(pin, GPIO.HIGH)  # Send HIGH signal
    GPIO.output(pin, GPIO.LOW)   # Reset to LOW

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/button_clicked', methods=['POST'])
def button_clicked():
    button = request.form['button']
    if button == 'button1':
        send_signal(17)  # Sending signal for button 1
    elif button == 'button2':
        send_signal(18)  # Sending signal for button 2
    return f"Signal sent to ESP32 for {button}"

if __name__ == '__main__':
    app.run(debug=True)
