# RBN-ROS2
## Connect the ESP32 and Raspberry Pi via UART for communication.
ESP32 TXD to Raspberry Pi RX (GPIO14 on ESP32 to GPIO15 on Raspberry Pi)
ESP32 RXD to Raspberry Pi TX (GPIO13 on ESP32 to GPIO14 on Raspberry Pi)
GND of ESP32 to GND of Raspberry Pi

## Connect the L9110S DC Motor Driver to the ESP32.

IN1 and IN2 of Motor 1 to GPIO pins on ESP32
IN3 and IN4 of Motor 2 to GPIO pins on ESP32
VCC and GND of Motor Driver to 5V and GND on ESP32 respectively
Connect the power source for the motors to the power supply


## Connect the buttons to GPIO pins on ESP32.

Connect one terminal of Button A to GPIO pin on ESP32
Connect the other terminal of Button A to GND on ESP32
Connect one terminal of Button B to GPIO pin on ESP32
Connect the other terminal of Button B to GND on ESP32

# Notes
Ensure you have the Flask library installed on your Raspberry Pi (pip install Flask).

Create a folder called templates in the same directory as your Python script, and inside it, create a file named index.html with your HTML code for the website.
This code will set up a Flask web server on your Raspberry Pi and communicate with the ESP32 over UART. The web page will have two buttons (Point A and Point B) which, when pressed, will send commands to the ESP32 to control the motors connected to the L9110S motor driver.

