from flask import Flask, render_template, request
import requests

app = Flask(__name__)

ESP32_IP = 'http://esp32_ip_address:port'  # Replace with your ESP32's IP and port

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/button', methods=['POST'])
def button():
    button_pressed = request.form['button']
    if button_pressed == '1':
        requests.post(f'{ESP32_IP}/button', data={'button': '1'})
    elif button_pressed == '2':
        requests.post(f'{ESP32_IP}/button', data={'button': '2'})
    return 'OK'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
