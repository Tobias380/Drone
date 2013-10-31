import RPi.GPIO as GPIO
import time
from Adafruit_PWM_Servo_Driver import PWM

GPIO.setmode (GPIO.BOARD)
pwm = PWM(0x40, debug=True)
GPIO.setup (7, GPIO.IN)              
GPIO.setup (15, GPIO.OUT)
GPIO.setup (16, GPIO.OUT)
GPIO.setup (18, GPIO.OUT)
GPIO.setup (22, GPIO.OUT)
GPIO.setup (12, GPIO.OUT)
GPIO.setup (13, GPIO.OUT)

              
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

def Average () :
    distance1= Measure()
    time.sleep(0.01)
    distance2= Measure()
    time.sleep(0.01)
    distance3= Measure()
    time.sleep(0.01)
    distance4= Measure()
    time.sleep(0.01)
    distance5= Measure()
    time.sleep(0.01)
    distance6= Measure()
    time.sleep(0.01)
    distance7= Measure()
    time.sleep(0.01)
    distance8= Measure()
    time.sleep(0.01)
    distance9= Measure()
    time.sleep(0.01)
    distance10= Measure()
    AvgDist= ((distance1 + distance2 + distance3 + distance4 + distance5 + distance6 + distance7 + distance8 + distance9 + distance10)/10)
    return AvgDist

#Start motors spinning
GPIO.output(16, True)
GPIO.output(22, False)
GPIO.output(12, True)
GPIO.output(13, False)
Motor1 = GPIO.PWM (15,600)
Motor2 = GPIO.PWM (18,600)
Motor1.start(0)
Motor2.start(0)

try:
    while (True):
        Height= Average()
        #print Height
        if (Height>10):
            Motor1.ChangeDutyCycle(10)
            Motor2.ChangeDutyCycle(10)
        if(Height<10):
            if(Height<9):
                if(Height<8):
                    if(Height<7):
                        if(Height<6):
                            if(Height<5):
                               print ('Landed')
                            else:
                                Motor1.ChangeDutyCycle(90)
                                Motor2.ChangeDutyCycle(90)
                        else:
                            Motor1.ChangeDutyCycle(75)
                            Motor2.ChangeDutyCycle(75)
                    else:
                        Motor1.ChangeDutyCycle(60)
                        Motor2.ChangeDutyCycle(60)
                else:
                    Motor1.ChangeDutyCycle(45)
                    Motor2.ChangeDutyCycle(45)
            else:
                Motor1.ChangeDutyCycle(30)
                Motor2.ChangeDutyCycle(30)
        time.sleep(0.01)
        
except KeyboardInterrupt :
                             Motor1.stop()
                             Motor2.stop()
                             GPIO.cleanup()
        
                             
                             

