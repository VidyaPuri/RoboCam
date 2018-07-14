from tkinter import *
from tkinter import font
from numpy import interp
import Adafruit_PCA9685
import time
PCA9685_pwm = Adafruit_PCA9685.PCA9685()
PCA9685_pwm.set_pwm_freq(60)

servo_min = [130,170,165,135,340,0]
servo_max = [570,550,480,540,800,0]

root = Tk()
var0 = DoubleVar()
var1 = DoubleVar()
servo0 = StringVar()
servo1 = StringVar()
font = font.Font(weight = "bold",size = 16)

def sel0():
    val=str(var0.get())
    selection = "Pos0 = " + val
    label0.config(text = selection)
    move_servo(0,val)

def sel1():
    val=str(var1.get())
    selection = "Pos1 = " + val
    label1.config(text = selection)
    move_servo(1,val)

def move_servo(servo,pos):
        print("Servo",servo,"moves to:",pos)
        PCA9685_pwm.set_pwm(servo,0,pos)
        time.sleep(1)



servo_label0 = Label(root,textvariable = servo0, relief = RAISED,bd=3,font = font)
servo0.set("Servo motor 0")
servo_label0.pack(anchor =W)
scale0 = Scale(root, variable = var0, from_=servo_min[0],to_=servo_max[0],orient=HORIZONTAL,length =300)
scale0.pack(anchor =W)
scale0.set((servo_min[0]+servo_max[0])/2)
button0 = Button(root, text = "Pos0 value", command = sel0,bd=3)
button0.pack(anchor =W)
label0= Label(root)
label0.pack()

servo_label1 = Label(root,textvariable = servo1, relief = RAISED,bd=3,font = font)
servo1.set("Servo motor 1")
servo_label1.pack(anchor =W)
scale1 = Scale(root, variable = var1,from_=servo_min[1],to_=servo_max[1],orient=HORIZONTAL,length =300)
scale1.pack(anchor =W)
scale1.set((servo_min[1]+servo_max[1])/2)
button1 = Button(root, text = "Pos1 value",command = sel1,bd=3)
button1.pack(anchor =W)

label1= Label(root)
label1.pack()


root.mainloop()
