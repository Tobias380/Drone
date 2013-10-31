import RPi.GPIO as GPIO
import time
from Adafruit_PWM_Servo_Driver import PWM

GPIO.setmode (GPIO.BOARD)
pwm = PWM(0x40, debug=True)
GPIO.setup (7, GPIO.IN)
GPIO.setup (11, GPIO.IN)

def Measure1 ():
    pwm.setPWMFreq(60)
    Echo1 =7
    pwm.setPWM(0,0,5)
    while GPIO.input(Echo1) == 0:
        pass
    start = time.time()
    while GPIO.input(Echo1) == 1:
        pass
    stop = time.time()
    pwm.setPWM(0,0,0)
    Distance1 =((stop- start)/0.000147)
    return Distance1

def Measure2 ():
    pwm.setPWMFreq(60)
    Echo2 =11
    pwm.setPWM(1,0,5)
    while GPIO.input(Echo2) == 0:
        pass
    start = time.time()
    while GPIO.input(Echo2) == 1:
        pass
    stop = time.time()
    pwm.setPWM(1,0,0)
    Distance2 =((stop- start)/0.000147)
    return Distance2

def Average (t) :
    distance1= Measure1()
    time.sleep(t)
    distance2= Measure2()
    time.sleep(t)
    distance3= Measure1()
    time.sleep(t)
    distance4= Measure2()
    time.sleep(t)
    distance5= Measure1()
    time.sleep(t)
    distance6= Measure2()
    time.sleep(t)
    distance7= Measure1()
    time.sleep(t)
    distance8= Measure2()
    time.sleep(t)
    distance9= Measure1()
    time.sleep(t)
    distance10= Measure2()
    AvgDist= ((distance1 + distance2 + distance3 + distance4 + distance5 + distance6 + distance7 + distance8 + distance9 + distance10)/10)
    #AvgDist= ((distance1 + distance2 + distance3)/3)

    return AvgDist
try:
    while (True):
        t= input ('Enter time gap: ')
        Height = Average(t)
        print ('Distance=', Height)
except KeyboardInterrupt :
    GPIO.cleanup()

