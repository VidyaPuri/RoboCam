import Adafruit_PCA9685
import time
PCA9685_pwm = Adafruit_PCA9685.PCA9685()
PCA9685_pwm.set_pwm_freq(60)

servo_min = [130,170,165,135,340,0]
servo_max = [570,550,480,540,800,0]

def start():
    print("You will move the servos to the desired position! Ready, steady, GO!")
    print("Enter servo number:")
    servo_fun()

def servo_fun():
    while True:
        try:
            a = int(input())
            if 0 <= a <= 5:
                servo = a
                print("Servo number is:",servo)
                break
            else:
                print("Wrong input, enter servo number between 0 and 5:")
        except ValueError:
            print("Invalid input. Value must be integer")
    pos_fun(servo)

def pos_fun(servo):
    print("Enter positon")
    while True:
        try:
            b = int(input())
            if servo_min[servo] <= b <= servo_max[servo]:
                pos = b
                print("Position is:",pos)
                break
            else:
                print("wrong input, enter number between",servo_min[servo], "and",servo_max[servo])
        except ValueError:
            print("invalid input. Value must be integer")
    print("Servo number",servo,"moves to position",pos)
    move_servo(servo,pos)

def move_servo(servo,pos):
        print("Servo numb:",servo,"moves for:",pos)
        PCA9685_pwm.set_pwm(servo,0,pos)
        time.sleep(2)
        start()
start()
