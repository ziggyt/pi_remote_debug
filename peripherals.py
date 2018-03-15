import lcd_i2c_driver
from RPi import GPIO
from subprocess import call
from time import sleep as delay

display = lcd_i2c_driver.lcd()


def handleInterrupt(channel):
    display.lcd_clear()
    display.lcd_display_string("Shutting down", 1)
    delay(1)
    display.lcd_clear()
    GPIO.cleanup()
    call("sudo nohup shutdown -h now", shell=True)
