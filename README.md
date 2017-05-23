# LED controller

Real time websockets LED controller with a PCA9685 board connected to a Raspberry Pi and some LED strips. Right now there is only one color-wheel with 3 channel outputs, however you can have up to 16 channels per board. All control is done via JSON, new channels and control options can be added with ease.

![screen shot 2015-12-22 at 09 11 53](https://cloud.githubusercontent.com/assets/1775702/11950815/3daffed4-a88c-11e5-9caa-8795266eba07.png)

## Setup
You will need a Raspberry Pi, a PCA9685 I2C PWM driver, some mosfets, and LEDs. I use [this board from Adafruit](https://www.adafruit.com/product/815), hooked up to some BUZ11 mosfets connected to a RGB LED 5m 5050 60led/m strip. To get the server running, you roughly need to do the following:

You will need a [Raspberry Pi running Raspbian Lite](https://www.raspberrypi.org/downloads/raspbian/). You can use [Etcher](https://etcher.io/) to easily flash your card with a graphical interface.

Once your Pi has booted up, you'll need to enable I2C:
```bash
sudo raspi-config
> 7 Advanced Options
> A7 I2C
> Yes
```

Then you you'll need to update your system and install smbus:
```bash
sudo apt-get update && sudo apt-get upgrade
sudo apt-get install python3-smbus
```

Next, clone and install this project:
```bash
git clone https://github.com/sasha42/LED-controller.git
cd LED-controller
pip install -r requirements.txt
````

You can then run `sudo python3 server.py` to run the controller. Sudo is required because you're accessing the system bus.

There may be a few more steps to do in case you've never used I2C with your Pi before, but those are fairly searchable. Some of the code in this repo has been borrowed improperly - please assume MVP status for this project.
