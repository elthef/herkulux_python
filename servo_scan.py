
import herkulex
from herkulex import servo

#connect to the serial port
print("Connecting....")
herkulex.connect("/dev/ttyUSB0",115200)
print("Connected only")
#scan for servos, it returns a tuple with servo id & model number
servos = herkulex.scan_servos()

print (servos)
