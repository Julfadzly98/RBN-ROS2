from flask import Flask, render_template, request
import requests

app = Flask(__name__)

html = '''
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Button Control</title>
  </head>
  <body>
    <form action="/send_signal" method="post">
      <input type="submit" name="button" value="Button 1">
      <input type="submit" name="button" value="Button 2">
    </form>
  </body>
</html>
'''

@app.route('/')
def index():
    return html

@app.route('/send_signal', methods=['POST'])
def send_signal():
    button_pressed = request.form['button']
    if button_pressed == 'Button 1':
        requests.get('http://ESP32_IP_ADDRESS/signal?button=1')
    elif button_pressed == 'Button 2':
        requests.get('http://ESP32_IP_ADDRESS/signal?button=2')
    return "Signal Sent!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
