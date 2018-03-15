import lcd_i2c_driver
from RPi import GPIO
from subprocess import call
from time import sleep as delay

display = lcd_i2c_driver.lcd()



def handleInterrupt(channel):
    countdown = 0
    display.lcd_clear()
    display.lcd_display_string("Shutting down", 1)

    for i in range(5):
        display.lcd_display_string(str(countdown), 2)
        countdown += countdown + 1
        delay(1)

    delay(1)
    display.lcd_clear()
    GPIO.cleanup()
    call("sudo nohup shutdown -h now", shell=True)
