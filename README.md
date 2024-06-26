# DisplayPi

#### Clone this repository to your Pi:
``` 
git clone https://github.com/devrema/DisplayPi.git
``` 

## Usage:

make sure that the OLED display is connected and.
you can test that by:

```
i2cdetect -y 1
```

Be careful with the display, as it can easily be damaged.


### Before executing:

Make sure to cofigure the path to your fonts in the script.
Use:
```
nano /path/to/Display.py
``` 
for configuration. 

#### You can use:
```python
font_path = None
```
if no fonts are installed.

Be also sure that the right drivers are being used. I use sh1106. This might not be the right option for your Display.
You should also reconfigure this as well, if you have rendering issues. (Aother driver is given in code: adafruit ssd1306)

#### You might as well install dependencies on your Pi.

``` 
sudo apt update
sudo apt install python3-pip
``` 
``` 
pip install <package-name>
``` 
####templates:
``` 
pip install pillow

pip install luma.core luma.oled luma.lcd luma.emulator

pip install psutil
``` 
#### this would be another driver

``` 
pip install adafruit-circuitpython-ssd1306 adafruit-circuitpython-framebuf
``` 
## Execute 
### use the command:
```
python3 /path/to/Display.py
```
For execution

## Automation

Go to root-dir.
Use:
```
sudo crontab -e
```

select 1 for nano editor, if you open it for the first time.

Add:

```
@Reboot python3 /path/to/Display.py &
```

Dont`t forget the "&"!


## Thats it. have fun!

## mind that you might have some issues with this code, since I use this code on my pi 3B+

e.g. most pip installations force you to use a virtual environment.
you might use other ports etc.




