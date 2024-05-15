import os
import psutil
from time import sleep
from PIL import Image, ImageDraw, ImageFont  # Hinzugefügt
from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import sh1106

# OLED-Display Initialisierung
serial = i2c(port=1, address=0x3C)
device = sh1106(serial)

# Laden einer Schriftart
font_size  = 12
font_path = "/usr/share/fonts/truetype/noto/NotoSans-Regular.ttf"  # Pfad zur Schriftartdatei
font = ImageFont.truetype(font_path, font_size)

# Funktion zur Anzeige der IP-Adresse und des Verbindungstyps
def get_ip_address():
    try:
        ip = os.popen('hostname -I').read().split()[0]
        if os.system("ping -c 1 google.com") == 0:
            connection_type = "LAN"
        else:
            connection_type = "WLAN"
    except:
        ip = "-.-.-.-"
        connection_type = "Unknown"
    return ip, connection_type

# Funktion zur Anzeige der Speichernutzung in %
def get_disk_usage():
    disk = psutil.disk_usage('/')
    disk_usage = disk.percent
    return disk_usage

# Funktion zur Anzeige der CPU-Auslastung und Temperatur
def get_cpu_usage_and_temp():
    cpu_usage = psutil.cpu_percent()
    cpu_temp = psutil

    # Funktion zur Anzeige der RAM-Auslastung
def get_ram_usage():
    ram = psutil.virtual_memory()
    ram_usage = ram.percent
    return ram_usage

def main():
    ip_address, connection_type = get_ip_address()
    cpu_usage, cpu_temp = get_cpu_usage_and_temp()
    ram_usage = get_ram_usage()
    disk_usage = get_disk_usage()

    ip_text = "Connection: {}".format(connection_type)
    cpu_text = "CPU: {:.1f}%".format(cpu_usage)
    temp_text = "T: {:.1f}°C".format(cpu_temp)
    ram_text = "RAM: {:.1f}%".format(ram_usage)
    disk_text = "Disk: {:.1f}%".format(disk_usage)

    while True:
        new_ip_address, new_connection_type = get_ip_address()
        new_cpu_usage, new_cpu_temp = get_cpu_usage_and_temp()
        new_ram_usage = get_ram_usage()
        new_disk_usage = get_disk_usage()

        img = Image.new("1", (device.width, device.height))
        draw = ImageDraw.Draw(img)

        if ip_address != new_ip_address or connection_type != new_connection_type:
            ip_address, connection_type = new_ip_address, new_connection_type
            ip_text = "Connection: {}".format(connection_type)

        if cpu_usage != new_cpu_usage:
            cpu_usage = new_cpu_usage
            cpu_text = "CPU: {:.1f}%".format(cpu_usage)

        if cpu_temp != new_cpu_temp:
            cpu_temp = new_cpu_temp
            temp_text = "T: {:.1f}°C".format(cpu_temp)

        if ram_usage != new_ram_usage:
            ram_usage = new_ram_usage
            ram_text = "RAM: {:.1f}%".format(ram_usage)

        if disk_usage != new_disk_usage:
            disk_usage = new_disk_usage
            disk_text = "Disk: {:.1f}%".format(disk_usage)

        # Erstelle ein Bild, das den aktuellen Inhalt des Displays darstellt
        draw.rectangle((0, 0, 128, 12), outline="black", fill="black")
        draw.text((4, 0), ip_text, fill="white", font=font)
        draw.rectangle((0, 24, 128, 48), outline="black", fill="black")
        draw.text((4, 12), "IP: {}".format(ip_address), fill="white", font=font)
        draw.rectangle((0, 36, 128, 48), outline="black", fill="black")
        draw.text((4, 24), cpu_text, fill="white", font=font)
        draw.rectangle((72, 36, 128, 48), outline="black", fill="black")
        draw.text((72, 24), temp_text, fill="white", font=font)
        draw.rectangle((0, 48, 128, 60), outline="black", fill="black")
        draw.text((4, 36), ram_text, fill="white", font=font)
        draw.rectangle((0, 60, 128, 72), outline="black", fill="black")
        draw.text((4, 48), disk_text, fill="white", font=font)

        # Aktualisiere das Display mit dem erstellten Bild
        device.display(img)

        # Warte 3 Sekunden, bevor die Informationen erneut angezeigt werden
        sleep(1)



if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass