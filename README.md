#LED controller

Real time websockets LED controller with a PCA9685 board connected to a Raspberry Pi and some LED strips. Right now there is only one color-wheel with 3 channel outputs, however you can have up to 16 channels per board. All control is done via JSON, new channels and control options can be added with ease.

![screen shot 2015-12-22 at 09 11 53](https://cloud.githubusercontent.com/assets/1775702/11950815/3daffed4-a88c-11e5-9caa-8795266eba07.png)

## Setup
You will need a Raspberry Pi, a PCA9685 I2C PWM driver, some mosfets, and LEDs. I use [this board from Adafruit](https://www.adafruit.com/product/815), hooked up to some BUZ11 mosfets connected to a RGB LED 5m 5050 60led/m strip. To get the server running, you roughly need to do the following:
```bash
sudo apt-get update && sudo apt-get upgrade
sudo apt-get install python3-smbus
pip3 install tornado
```
You can then run `sudo python3 server.py` to run the controller. Sudo is required because you're accessing the system bus.

There may be a few more steps to do in case you've never used I2C with your Pi before, but those are fairly searchable. Some of the code in this repo has been borrowed improperly - please assume MVP status for this project.
