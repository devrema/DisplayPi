# DisplayPi

Clone this repository to your Pi:
``` 
git clone https://github.com/devrema/DisplayPi.git
``` 


## Usage:

make sure that the OLED display is connected.
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
You should also reconfigure this as well, if you have rendering issues.

You might as well install dependencies on your Pi.
``` 
sudo apt update
sudo apt install python3-pip
``` 
``` 
pip install <package-name>
``` 
## Execute 
### use the command:
```
python3 /path/to/Display.py
```
For execution

## Automation

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




