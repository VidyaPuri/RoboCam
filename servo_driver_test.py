import Adafruit_PCA9685
import time
PCA9685_pwm = Adafruit_PCA9685.PCA9685()

PCA9685_pwm.set_pwm_freq(60)

servo_min = 125
servo_max = 540
pos4  = 300

def set_servo4(a,b):
    print("Servo1: ",a)
    PCA9685_pwm.set_pwm(4,0,a)
    return "Servo4:",a
    time.sleep(1)
    PCA9685_pwm.set_pwm(4,0,b)
    print("min")


for x in range(0,100):_
    set_servo4(servo_max,servo_min)
print("done")
