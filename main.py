# To add SMBus support to the raspberry pi enter this commands to the terminal: 
#                   sudo apt-get install python-smbus
#                   sudo apt-get install i2c-tools

# to check if board connected use: 
#                   sudo i2cdetect -y 0

# install the library: 
#                     sudo pip3 install adafruit-circuitpython-servokit

# to set servo angle i've used servos attached to pins 1-4:
# kit.servo[0].angle = ???          // base connect
# kit.servo[1].angle = ???          // middle left servo (forward, backword)
# kit.servo[2].angle = ???          // middle right servo (up, down)
# kit.servo[3].angle = ???          // tongs servo (open, close)

#  converting one range to other range
# new_value = ( (old_value - old_min) / (old_max - old_min) ) * (new_max - new_min) + new_min
# new_value = ( (50 - 90) / (180 - 90) ) * (100 - 0) + 0
# (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min;

# convert the range of input values to match the servos range
# acceptiong from 0 to 100 for any servo
def rangeConverter(value, in_min=0, in_max=100, out_min=90, out_max=180):
    return (value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)


class Arm:
    def moveLeft(self, angle):
        self.kit.servo[0].angle = rangeConverter(self.angle)

    def moveRight(self, angle):
        self.kit.servo[0].angle = rangeConverter(self.angle, out_min=0, out_max=90)

    def moveUp(self, angle):
        self.kit.servo[1].angle = rangeConverter(self.angle)

    def moveDown(self, angle):
        self.kit.servo[1].angle = rangeConverter(self.angle, out_min=0, out_max=90)

    def moveForward(self, angle):
        self.kit.servo[2].angle = rangeConverter(self.angle)

    def moveBackword(self, angle):
        self.kit.servo[2].angle = rangeConverter(self.angle, out_min=0, out_max=90)

    def take(self, angel):
        self.kit.servo[3].angle = rangeConverter(self.angle, in_min=0, in_max=100, out_min=0, out_max=180)