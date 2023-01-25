import RPi.GPIO as GPIO
from adafruit_mcp3xxx.analog_in import AnalogIn

from helpers import *

class AnalogSensor:
    """
    Generic analog sensor.
    """
    def __init__(self, mcp, channelNumber: int):
        """
        Returns a generic AnalogSensor object, with the output at an MCP3008 channel.
        Base class.
        """
        self.channelID = getChannel(channelNumber)
        self.channel = AnalogIn(mcp, self.channelID)

    def voltage(self):
        """
        Returns the analog channel voltage.
        """
        return self.channel.voltage

    def value(self):
        """
        Override this to convert voltage into meaningful reading.
        """
        return

class pHSensor(AnalogSensor):
    """
    Extends the AnalogSensor class for a pH sensor.
    Probe used: KPE-03.
    Board: pH-4502C
    """
    def __init__(self, mcp, channelNumber: int):
        """
        Create a pH sensor object.
        """
        super().__init__(mcp, channelNumber)

    def value(self):
        """
        Implements the following formula:
        pH = (-8.363 * voltage) + 21.34.
        Calculated based on a formula found online, scaled down for 3.3V
        """
        v = self.voltage()
        c1 = -8.363
        c2 = 21.34
        return (c1 * v) + c2

class TDSSensor(AnalogSensor):
    """
    Extends the AnalogSensor class for a TDS sensor.
    Board: TDS meter v1.0
    """
    def __init__(self, mcp, channelNumber: int):
        """
        Create a TDS Sensor object.
        """
        super().__init__(mcp, channelNumber)

    def value(self):
        """
        Simply maps the 0-2.3V output range to 0-1000 TDS range.
        """
        return (self.voltage() / 2.3) * 1000

class WaterLevelSensor(AnalogSensor):
    """
    Generic water level depth sensor with exposed traces.
    """
    def __init__(self, mcp, channelNumber: int, power: int):
        """
        This sensor must be turned on before use and switched off after use.
        This is done to prevent corrosion.
        """
        super().__init__(mcp, channelNumber)
        
        self.power = power
        self.isActive = False
        
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.power, GPIO.OUT)

        self.switch_off()

    def switch_on(self):
        """
        Switches the sensor on.
        """
        GPIO.output(self.power, 1)
        self.isActive = True

    def switch_off(self):
        """
        Switches the sensor off.
        """
        GPIO.output(self.power, 0)
        self.isActive = False

    def voltage(self):
        return super().voltage()

    def value(self):
        """
        Simply maps the 0-3.3V output range to 0-100 % range.
        """
        return (self.voltage() / 3.3) * 100

class Pump:
    """
    A generic pump object, controlled by a TIP122. Only supports switching on and off but PWM control is possible.
    """
    def __init__(self, pin: int):
        """
        Returns a pump object.
        """
        self.pin = pin
        self.isActive = False

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)

        self.deactivate()
    
    def activate(self):
        """
        Switches the pump on.
        """
        GPIO.output(self.pin, 1)
        self.isActive = True

    def deactivate(self):
        """
        Switches the pump off.
        """
        GPIO.output(self.pin, 0)
        self.isActive = False
    
    def toggle(self):
        """
        Toggles the pump.
        """
        if self.isActive: 
            GPIO.output(self.pin, 0)
        else:
            GPIO.output(self.pin, 1)

        self.isActive = not self.isActive