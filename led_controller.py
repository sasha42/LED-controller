# how to class from http://www.jesshamrick.com/2011/05/18/an-introduction-to-classes-and-inheritance-in-python/

#######################################
## LED controller configuration test ##
#######################################
#
# Toying around with ideas on how to control multiple different types of
# LEDs from using a single library. There is a Light class that is 
# inherited by subsequent chip specific classes that actually drive the
# LEDs.
#
# The LEDs are then controlled by calling their variable, with the
# desired function (and optionally parameters). The idea is that the code
# is more modular and enables more flexibility for designing controllable
# light interfaces.
#

class Light(object):
    """ Shared class for LED Light sections """

    def ___init___(self, name, parameters):
        self.name = name
        self.parameters = self.parameters

class apa102(Light):
    """ apa102 addressable led strips over spi protocol """

    def __init__(self, name, start_led, end_led):
        Light.__init__(self, name, [start_led, end_led])
        self.start_led = start_led
        self.end_led = end_led

    def rainbow():

    def theater_chase():

    def left_signal():

    def right_signal():

    def perlin_noise():

    def solid_color():

    def color_history():

class pca9685(Light):
    """ pca9685 pwm i2c driver for large installations """

    def __init__(self, name, i2c_address, channels):
        Light.__init__(self, name, [i2c_address, channels])
        self.i2c_address = i2c_address
        self.channels = channels

    def rainbow():

    def solid_color():


# first the light setup is created
lights = []

# sections represent strip configurations with name and parameters
east_window = pca9685("east_window", 0x40, {0: "red", 1: "green", 2: "blue"})
west_window = apa102("west_window", 0, 200)

# append secrions to light setup
lights.append(east_window, west_window)

class Light(object):
    """ Shared class for LED Light sections """

    def ___init___(self, name, parameters):
        self.name = name
        self.parameters = self.parameters

class apa102(Light):
    """ apa102 addressable led strips over spi protocol """

    def __init__(self, name, start_led, end_led):
        Light.__init__(self, name, [start_led, end_led])
        self.start_led = start_led
        self.end_led = end_led

    def rainbow():

    def theater_chase():

    def left_signal():

    def right_signal():

    def perlin_noise():

    def solid_color():

    def color_history():

class pca9685(Light):
    """ pca9685 pwm i2c driver for large installations """

    def __init__(self, name, i2c_address, channels):
        Light.__init__(self, name, [i2c_address, channels])
        self.i2c_address = i2c_address
        self.channels = channels

    def rainbow():

    def solid_color():


# first the light setup is created
lights = []

# sections represent strip configurations with name and parameters
east_window = pca9685("east_window", 0x40, {0: "red", 1: "green", 2: "blue"})
west_window = apa102("west_window", 0, 200)

# append secrions to light setup
lights.append(east_window, west_window)


#### what the controls will look like
west_window.theater_chase()
sleep(10)
west_window.solid_color(0xFFFFFF)
