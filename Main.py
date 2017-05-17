import RPi.GPIO as GPIO
from time import sleep as sleep

state = 1
speed = 50
       
GPIO.setmode(GPIO.BOARD)

def set(property, val):
        f = open("/sys/class/rpi-pwm/pwm0/" + property, 'w')
        f.write(val)
        f.close()

set("deleyed, 0")
set("mode, pwm")
set("active, 1")
set("frequency, 500")

def worker:
       if(state = 3):
              global state = 1
       else:
              global state = state + 1
              
       if(state = 1):
              global speed = 50
       elif(state = 2):
              global speed = 70
       elif(state = 3):
              global speed = 90
       GPIO.output(motor_1, True)
       GPIO.output(motor_1, False)
       set("duty", str(speed))
       #monitor(state)
       sleep(60)
       
#def monitor:
while True:
       worker()
       
