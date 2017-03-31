#1/usr/bin/pythonRoot

gpio_root = '/sys/class/gpio'
gpio_name = 'gpiochip0'

import os
import time

def get_gpio_count(gpio_root, gpio_name):
  """Returns the number of gpios available"""
  with open(os.path.join(gpio_root, gpio_name, 'ngpio') as f:
                         return int(f.read().rstrip())

def export(gpio_root, gpio_name, gpio_number):
    """Instructs the kernel to load and configure the driver for gpio pin"""
    gpio_count = get_gpio_count(gpio_root, gpio_name)
    if gpio_number < 0 or gpio_number > gpio_count-1:
        raise RuntimeError("Specified GPIO is out of range")

    with open(os.path.join(gpio_root, gpio_name, 'base')) as f:
        gpio_base = int(f.read().rstrip())

    gpio_addr = gpio_base + gpio_number
    gpio_folder = "gpio" + str(gpio_addr)

    if not os.path.exists(os.path.join(gpio_root, gpio_folder)):
            with open(os.path.join(gpio_root, 'export'), 'w') as f:
                f.write(str(gpio_addr))

    return gpio_folder, gpio_addr

def set_gpio(gpio_root, gpio_name, gpio_number, value):
    """Turns a gpio on or off"""
    gpio_folder, gpio_addr = export_gpio(gpio_root, gpio_name, gpio_number)

    with open(os.path.join(gpio_root, gpio_folder, 'direction'), 'w') as f:
        f.write("out")
    with open(os.path.join(gpio_root, gpio_folder, 'value'), 'w') as f:
        f.write(str(1 if (value != 0) else 0)

if __name__ == "__main__":
    #count = get_gpio_count(gpio_root, gpio_name)
    set_gpio(gpio_root, gpio_name, 54, 1)
"""
    #first we turn them all on
    for i in range(count):
        set_gpio(gpio_root, gpio_name, i, 1)
    time.sleep(2)

    #now we make a cool pattern!
    ticker = 0
    direction = 1
    while 1:
        for i in range(count):
            if ticker == i:
                set_gpio(gpio_root, gpio_name, i, 1)
            else:
                set_gpio(gpio_root, gpio_name, i, 0)
                
        ticker += direction
        if ticker == 0 or ticker == 3:
                direction *= -1
                
        time.sleep(0.5) """
