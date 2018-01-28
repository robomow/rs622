import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(4,GPIO.IN,pull_up_down=GPIO.PUD_UP)

#p = GPIO.PWM(11,50)
#p.start(7.5)

try:
    prev_input = 0
    while True:
      input = GPIO.input(4)
      print("Input="+str(input))
      if ((not prev_input) and input):
        print("Button Pressed")
      prev_input = input
      #p.ChangeDutyCycle(7.5)
      #time.sleep(1)
      #p.ChangeDutyCycle(12.5)
      #time.sleep(1)
      #p.ChangeDutyCycle(2.5)
      time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()

