from flask import Flask, render_template
import requests

app = Flask(__name__)

ESP32_IP = "ESP32_IP_ADDRESS"  # Replace with the actual IP address of your ESP32

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/control/<action>')
def control(action):
    url = f"http://{ESP32_IP}/{action}"
    response = requests.get(url)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
