import Adafruit_PCA9685
PCA9685_pwm = Adafruit_PCA9685.PCA9685()

PCA9685_pwm.set_pwm_freq(60)

servo_min = 125
servo_max = 540
pos4  = 300

def main():
    set_servo4(pos4)
    print("over")

def set_servo4(a):
    print("Servo1: ",a)
    PCA.set_pwm(4,0,a)
    return "Servo4:",a

if __name__ == '__main__':
    main()
