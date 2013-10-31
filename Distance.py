import RPi.GPIO as GPIO
import time
from Adafruit_PWM_Servo_Driver import PWM

GPIO.setmode (GPIO.BOARD)
pwm = PWM(0x40, debug=True)
GPIO.setup (7, GPIO.IN)


def Measure ():
    pwm.setPWMFreq(60)
    Echo =7
    pwm.setPWM(0,0,410)
    while GPIO.input(Echo) == 0:
        pass
    start = time.time()
    while GPIO.input(Echo) == 1:
        pass
    stop = time.time()
    Distance =((stop- start)/0.000147)
    return Distance

def Average (t) :
    distance1= Measure()
    time.sleep(t)
    distance2= Measure()
    time.sleep(t)
    distance3= Measure()
    time.sleep(t)
    distance4= Measure()
    time.sleep(t)
    distance5= Measure()
    time.sleep(t)
    distance6= Measure()
    time.sleep(t)
    distance7= Measure()
    time.sleep(t)
    distance8= Measure()
    time.sleep(t)
    distance9= Measure()
    time.sleep(t)
    distance10= Measure()
    AvgDist= ((distance1 + distance2 + distance3 + distance4 + distance5 + distance6 + distance7 + distance8 + distance9 + distance10)/10)
    return AvgDist
try:
while (True):
    t= input ('Enter time gap: ')
    Height = Average(t)
    Print ('Distance=', Height)
    except KeyboardInterrupt :
gpio.cleanup()

