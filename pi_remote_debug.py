import RPi.GPIO as GPIO
import Adafruit_DHT as dht
import lcd_i2c_driver
import peripherals


#### Declarations

buttonPin = 17
dhtPin = 26

#### GPIO SETUP

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(buttonPin, GPIO.IN, GPIO.PUD_UP)

#### INTERRUPTS

GPIO.add_event_detect(buttonPin, GPIO.FALLING, callback=peripherals.handleInterrupt, bouncetime=300)

#### INITIALIZATIONS

display = lcd_i2c_driver.lcd()
sensor = dht.DHT11


def printDht():
    h, t = dht.read_retry(sensor, dhtPin)
    display.lcd_display_string("Temp: " + str(t) + "C", 1)
    display.lcd_display_string("Humidity: " + str(h) + "%", 2)


def main():
    printDht()
    main()


main()
