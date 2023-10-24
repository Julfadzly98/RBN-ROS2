from flask import Flask, request

app = Flask(__name__)

@app.route('/button1', methods=['POST'])
def button1():
    print("Button 1 pressed")
    # Code to handle button 1 press
    return 'Button 1 pressed'

@app.route('/button2', methods=['POST'])
def button2():
    print("Button 2 pressed")
    # Code to handle button 2 press
    return 'Button 2 pressed'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
