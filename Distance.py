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

def Average1 () :
    distance1= Measure1()
    time.sleep(0.01)
    distance2= Measure1()
    time.sleep(0.01)
    distance3= Measure1()
    time.sleep(0.01)
    distance4= Measure1()
    time.sleep(0.01)
    distance5= Measure1()
    time.sleep(0.01)
    distance6= Measure1()
    time.sleep(0.01)
    distance7= Measure1()
    time.sleep(0.01)
    distance8= Measure1()
    time.sleep(0.01)
    distance9= Measure1()
    time.sleep(0.01)
    distance10= Measure1()
    AvgDist= ((distance1 + distance2 + distance3 + distance4 + distance5 + distance6 + distance7 + distance8 + distance9 + distance10)/10)
    #AvgDist= ((distance1 + distance2 + distance3)/3)
    Tolerance=AvgDist*0.1
    if abs(distance1- AvgDist)> Tolerance
       print ('Tolerance difference')
    if abs(distance2- AvgDist)> Tolerance
       print ('Tolerance difference')
    if abs(distance3- AvgDist)> Tolerance
       print ('Tolerance difference')
    if abs(distance4- AvgDist)> Tolerance
       print ('Tolerance difference')
    if abs(distance5- AvgDist)> Tolerance
       print ('Tolerance difference')
    if abs(distance6- AvgDist)> Tolerance
       print ('Tolerance difference')
    if abs(distance7- AvgDist)> Tolerance
       print ('Tolerance difference')
    if abs(distance8- AvgDist)> Tolerance
       print ('Tolerance difference')
    if abs(distance9- AvgDist)> Tolerance
       print ('Tolerance difference')
    if abs(distance10- AvgDist)> Tolerance
       print ('Tolerance difference')
      
    return AvgDist

def Average2 () :
    distance1= Measure2()
    time.sleep(0.01)
    distance2= Measure2()
    time.sleep(0.01)
    distance3= Measure2()
    time.sleep(0.01)
    distance4= Measure2()
    time.sleep(0.01)
    distance5= Measure2()
    time.sleep(0.01)
    distance6= Measure2()
    time.sleep(0.01)
    distance7= Measure2()
    time.sleep(0.01)
    distance8= Measure2()
    time.sleep(0.01)
    distance9= Measure2()
    time.sleep(0.01)
    distance10= Measure2()
    AvgDist= ((distance1 + distance2 + distance3 + distance4 + distance5 + distance6 + distance7 + distance8 + distance9 + distance10)/10)
    #AvgDist= ((distance1 + distance2 + distance3)/3)
    Tolerance=AvgDist*0.1
    if abs(distance1- AvgDist)> Tolerance
       print ('Tolerance difference')
    if abs(distance2- AvgDist)> Tolerance
       print ('Tolerance difference')
    if abs(distance3- AvgDist)> Tolerance
       print ('Tolerance difference')
    if abs(distance4- AvgDist)> Tolerance
       print ('Tolerance difference')
    if abs(distance5- AvgDist)> Tolerance
       print ('Tolerance difference')
    if abs(distance6- AvgDist)> Tolerance
       print ('Tolerance difference')
    if abs(distance7- AvgDist)> Tolerance
       print ('Tolerance difference')
    if abs(distance8- AvgDist)> Tolerance
       print ('Tolerance difference')
    if abs(distance9- AvgDist)> Tolerance
       print ('Tolerance difference')
    if abs(distance10- AvgDist)> Tolerance
       print ('Tolerance difference')

    return AvgDist

try:
    while (True)
        Height1 = Average1()
        Height2 = Average2()
        print ('Distance=', Height1)
        print ('Distance=', Height2)
except KeyboardInterrupt :
    GPIO.cleanup()

