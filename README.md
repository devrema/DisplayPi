# DisplayPi

Clone this repository to your Pi:
git clone https://github.com/devrema/DisplayPi.git


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
You can use:
``` 
font_path = None
```
if no fonts are installed.

Be also sure to use the right driver. I use sh1106. This might not be the right option for your purpose.
You should also reconfigure this as well, if you have rendering issues.


### use the command:

```
python3 /path/to/Display.py
```


## Automation

Use 
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




