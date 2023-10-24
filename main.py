# Install Flask if not already installed: pip install Flask
from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <form action="/send_signal" method="post">
        <input type="submit" value="Send Signal">
    </form>
    '''

@app.route('/send_signal', methods=['POST'])
def send_signal():
    # Send a request to ESP32
    response = requests.get('http://esp32_ip_address:port/receive_signal')
    return response.text

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
