#1/usr/bin/pythonRoot

gpio_root = '/sys/class/gpio'
gpio_name = 'gpiochip0'

import os
import time

def get_gpio_count(gpio_root, gpio_name):
  """Returns the number of gpios available"""
  f = open(os.path.join(gpio_root, gpio_name, 'ngpio'))
  num = int(f.read().rstrip())
  f.close()
  return num

def export(gpio_root, gpio_name, gpio_number):
  """Instructs ther kernel to load and configure the driver for gpio pin"""
  gpio_count = get_gpio_count(gpio_root, gpio_name)
  if gpio_number < 0 or gpio_number > gpio_count-1:
    raise RuntimeError("Specified GPIO is out of range")

  f = open(os.path.join(gpio_root, gpio_name, 'base'))
  gpio_base = int(f.read().rstrip())
  f.close()

  gpio_addr = gpio_base + gpio_number
  gpio_folder = "gpio" + str(gpio_addr)

  if not os.path.exists(os.path.join(gpio_root, gpio_folder)):
    f = open(os.path.join(gpio_root, 'export'), 'w')
    f.write(str(gpio_addr))
    f.close()

  return gpio_folder, gpio_addr

def set_gpio(gpio_root, gpio_name, gpio_number, value):
  """Turns a gpio on or off"""
  gpio_folder, gpio_addr = export(gpio_root, gpio_name, gpio_number)

  f = open(os.path.join(gpio_root, gpio_folder, 'direction'), 'w')
  f.write("out")
  f.close()

  f = open(os.path.join(gpio_root, gpio_folder, 'value'), 'w')
  f.write(str(1 if (value != 0) else 0))
  f.close()

def set_value(num, value):
  set_gpio(gpio_root, gpio_name, num, value)

def main():
  while (True):

    key = raw_input("Enter 'w' for On, 's' for Off and any other key to quit.")

    if key == "w":

      set_value(54, 1)
      set_value(55, 1)
      set_value(56, 1)
      set_value(57, 1)

    elif key == "s":

      set_value(54, 0)
      set_value(55, 0)
      set_value(56, 0)
      set_value(57, 0)

    else:

      break

if __name__ == "__main__":
    main()
