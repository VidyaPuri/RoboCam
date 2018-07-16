from tkinter import *
from tkinter import font
from numpy import interp
import Adafruit_PCA9685
import time
import XboxController
PCA9685_pwm = Adafruit_PCA9685.PCA9685()
PCA9685_pwm.set_pwm_freq(60)

servoMin = [130,170,165,135,340,0]
servoMax = [570,550,480,540,800,0]

contMin =[-100,-100,0,-100,-100,0]
contMax =[100,100,100,100,100,100]

startPos =[350,360,325,340,500,0]
currentPos = startPos
root = Tk()
var0 = DoubleVar()
var1 = DoubleVar()
var2 = DoubleVar()
var3 = DoubleVar()
var4 = DoubleVar()
var5 = DoubleVar()
servo0 = StringVar()
servo1 = StringVar()
servo2 = StringVar()
servo3 = StringVar()
servo4 = StringVar()
servo5 = StringVar()
ifGrad = False
servoId =[0,1,4,3,2,5,6,7,8,9,10,11,12,13,14,15,16,17]
step=0.1

font = font.Font(weight = "bold",size = 16)
def init():
    print("Initialisation, robot goes to mid position on all servos")
    for i in range(0,5):
        moveServo(i,startPos[i])
        print("Servo",i,"is at pos",startPos[i])
    #print("ifGrad",ifGrad)


def mapFromTo(x,a,b,c,d): #maps range from a - b = input range c - d = output range
    y=(x-a)/(b-a)*(d-c)+c
    return y

def myCallBack(controlId,Value):
    global ifGrad
    controlId=servoId[controlId]
    if controlId == 8:
        if Value == 1:
            ifGrad = not ifGrad
            init()
            #print("ifGrad",ifGrad)
    if controlId<=5:
        #print("Control id:",controlId,"Value:",Value)
        #move_servo(controlId,servoPos)
        move(controlId,Value,ifGrad)

def move(controlId,Value,ifGrad):
    if ifGrad == True:
        moveGrad(controlId,Value)
    elif ifGrad == False:
        servoPos = mapFromTo(Value,contMin[controlId],contMax[controlId],servoMin[controlId],servoMax[controlId])
        servoPos = int(servoPos)
        moveServo(controlId,servoPos)

def moveServo(servo,pos):
        print("Servo",servo,"moves to:",pos)
        PCA9685_pwm.set_pwm(servo,0,pos)
        #time.sleep(1)
def moveGrad(servo,pos):
    if servo == 2:
        servoPos2 = mapFromTo(pos,contMin[servo],contMax[servo],-100,100)
        currentPos[2] = currentPos[2] + servoPos2*step
        if currentPos[2]>=servoMax[2]:
            currentPos[2] = servoMax[2]
        elif currentPos[2]<=servoMin[2]:
            currentPos[2]=servoMin[2]
        currentPos[2] = int(currentPos[2])
        #print("Servo",servo,"moves to:",currentPos[2])
        #PCA9685_pwm.set_pwm(servo,0,currentPos[servo])
    else:
        currentPos[servo] = currentPos[servo]+ pos*step
        if currentPos[servo]>=servoMax[servo]:
            currentPos[servo] = servoMax[servo]
        elif currentPos[servo]<=servoMin[servo]:
            currentPos[servo]=servoMin[servo]
        currentPos[servo] = int(currentPos[servo])
        #print("Servo",servo,"moves to:",currentPos[servo])
    PCA9685_pwm.set_pwm(servo,0,currentPos[servo])
    print("Servo",servo,"moves to:",currentPos[servo])
init()

xboxCont = XboxController.XboxController(
        controllerCallBack = myCallBack,
        joystickNo = 0,
        deadzone = 30,
        scale = 100,
        invertYAxis = False)
try:
    xboxCont.start()
    print("xbox controller running")
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("user canceled")
    xboxCont.stop()
"""
def fun(button):
    if button == 0:
        val=str(var0.get())
        selection = "Pos",button," = " + val
        label0.config(text = selection)
    elif button == 1:
        val=str(var1.get())
        selection = "Pos",button," = " + val
        label1.config(text = selection)
    elif button == 2:
        val=str(var2.get())
        selection = "Pos",button," = " + val
        label2.config(text = selection)
    elif button == 3:
        val=str(var3.get())
        selection = "Pos",button," = " + val
        label3.config(text = selection)
    elif button == 4:
        val=str(var4.get())
        selection = "Pos",button," = " + val
        label4.config(text = selection)
    elif button == 5:
        val=str(var5.get())
        selection = "Pos",button," = " + val
        label5.config(text = selection)
    val=int(float(val))
    move_servo(button,val)

def move_servo(servo,pos):
        print("Servo",servo,"moves to:",pos)
        #PCA9685_pwm.set_pwm(servo,0,pos)
        time.sleep(1)

servo_label0 = Label(root,textvariable = servo0, relief = RAISED,bd=3,font = font)
servo0.set("Servo motor 0")
servo_label0.pack(anchor =W)
scale0 = Scale(root, variable = var0, from_=servo_min[0],to_=servo_max[0],orient=HORIZONTAL,length =300)
scale0.pack(anchor =W)
scale0.set((servo_min[0]+servo_max[0])/2)
button0 = Button(root, text = "Pos0 value", command = lambda: fun(0),bd=3)
button0.pack(anchor =W)
label0= Label(root)
label0.pack()

servo_label1 = Label(root,textvariable = servo1, relief = RAISED,bd=3,font = font)
servo1.set("Servo motor 1")
servo_label1.pack(anchor =W)
scale1 = Scale(root, variable = var1,from_=servo_min[1],to_=servo_max[1],orient=HORIZONTAL,length =300)
scale1.pack(anchor =W)
scale1.set((servo_min[1]+servo_max[1])/2)
button1 = Button(root, text = "Pos1 value",command = lambda: fun(1),bd=3)
button1.pack(anchor =W)
label1= Label(root)
label1.pack()

servo_label2 = Label(root,textvariable = servo2, relief = RAISED,bd=3,font = font)
servo2.set("Servo motor 2")
servo_label2.pack(anchor =W)
scale2 = Scale(root, variable = var2,from_=servo_min[2],to_=servo_max[2],orient=HORIZONTAL,length =300)
scale2.pack(anchor =W)
scale2.set((servo_min[2]+servo_max[2])/2)
button2 = Button(root, text = "Pos2 value",command = lambda: fun(2),bd=3)
button2.pack(anchor =W)
label2= Label(root)
label2.pack()

servo_label3 = Label(root,textvariable = servo3, relief = RAISED,bd=3,font = font)
servo3.set("Servo motor 3")
servo_label3.pack(anchor =W)
scale3 = Scale(root, variable = var3,from_=servo_min[3],to_=servo_max[3],orient=HORIZONTAL,length =300)
scale3.pack(anchor =W)
scale3.set((servo_min[3]+servo_max[3])/2)
button3 = Button(root, text = "Pos3 value",command = lambda: fun(3),bd=3)
button3.pack(anchor =W)
label3= Label(root)
label3.pack()

servo_label4 = Label(root,textvariable = servo4, relief = RAISED,bd=3,font = font)
servo4.set("Servo motor 4")
servo_label4.pack(anchor =W)
scale4 = Scale(root, variable = var4,from_=servo_min[4],to_=servo_max[4],orient=HORIZONTAL,length =300)
scale4.pack(anchor =W)
scale4.set((servo_min[4]+servo_max[4])/2)
button4 = Button(root, text = "Pos4 value",command = lambda: fun(4),bd=3)
button4.pack(anchor =W)
label4= Label(root)
label4.pack()

servo_label5 = Label(root,textvariable = servo5, relief = RAISED,bd=3,font = font)
servo5.set("Servo motor 5")
servo_label5.pack(anchor =W)
scale5 = Scale(root, variable = var5,from_=servo_min[5],to_=servo_max[5],orient=HORIZONTAL,length =300)
scale5.pack(anchor =W)
scale5.set((servo_min[5]+servo_max[5])/2)
button5 = Button(root, text = "Pos5 value",command = lambda: fun(5),bd=3)
button5.pack(anchor =W)
label5= Label(root)
label5.pack()

root.mainloop()
"""
