import Adafruit_PCA9685
PCA9685_pwm = Adafruit_PCA9685.PCA9685()

PCA9685_pwm.set_pwm_freq(60)

servo_min = 125
servo_max = 540
pos4  = 300

while True:
    pos4=servo_max
    set_servo4(pos4)
    print("max")
    time.sleep(100)
    pos4=servo_min
    set_servo4(pos4)
    print("min")

def set_servo4(a):
    print("Servo1: ",a)
    PCA9685_pwm.set_pwm(4,0,a)
    return "Servo4:",a
