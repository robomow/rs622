import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(4,GPIO.IN,pull_up_down=GPIO.PUD_UP)

p = GPIO.PWM(17,50)
p.start(7.5)

try:
    pushedDown = 0
    releasedUp = 1
    prev_input = 0
    while True:
      input = GPIO.input(4)
      #print("Input="+str(input))
      if ((not pushedDown) and input):
           print("Button Pressed Down rotating 90 degrees")
           print("Input="+str(input))
           p.ChangeDutyCycle(2.5) #90
           time.sleep(1)
           pushedDown = 1
           releasedUp = 1
      elif ((releasedUp) and not input):
           print("Button Released rotating -90 degrees")
           print("Input="+str(input))
           p.ChangeDutyCycle(12.5) #-90
           time.sleep(1)
           releasedUp = 0
           pushedDown = 0

      #p.ChangeDutyCycle(7.5) #0
      #time.sleep(1)
      #p.ChangeDutyCycle(14.5) #-90
      #time.sleep(1)
      #p.ChangeDutyCycle(2.5) #90
      #time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()

