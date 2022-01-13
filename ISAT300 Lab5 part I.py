#********************************************************************
#   importing packages already on the RPi into this Python program  *
#********************************************************************

import board
import busio
import digitalio
import adafruit_max31856

#***********************************
#   Setting up the thermocouple    *
#***********************************

# create an SPI object
spi = busio.SPI(board.SCK, board.MOSI, board.MISO)

# allocate a Chip Select pin for the thermocouple (CS pin) and set the direction
cs = digitalio.DigitalInOut(board.D5)
cs.direction = digitalio.Direction.OUTPUT

# create a thermocouple object with the above
thermocouple = adafruit_max31856.MAX31856(spi, cs)

#*******************************************************************
#**    reading the thermocouple and printing output on screen      *
#*******************************************************************

print(thermocouple.temperature, "C")
print(str(thermocouple.temperature * 9 / 5 + 32), "F")
