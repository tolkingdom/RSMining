import pyautogui
from random import uniform,randint
import bezmouse



#defining global variables and determining mouse coordinates
x0,y0 = calibrate()
bottomright = x0+765,y0+502
client=(x0,y0,765,502)
textnotif=(x0+3,y0+440,236,25)
gamewindow=(x0+5,y0+4,515,334)
inventory=(x0+549,y0+210,183,253)
motionbox=(x0+300,y0,45,45)
mapbox=(x0+568,y0+11,151,151)
bankdep = (228,83,83),(227,82,82)

while True:
    getOre()
    checkRun()
    toBank()
    checkRun()
    fromBank()


def getOre():


#Find runelite logo and calibrate x,y mouse positions
def calibrate():
    l,t,w,h = imgmatchscreen('img/runelite.png')
    print ("calibrated to : " + str((l,t,w,h)))
    return l,t+27

#right click with random pause intervals
def humanrclick():
    timer=(uniform(0.01,0.015))
    time.sleep((timer/2) - 0.00005)
    pyautogui.mouseDown(button='right')
    time.sleep(timer)
    pyautogui.mouseUp(button='right')
    time.sleep((timer/2) - 0.00009)

#left click with random pause intervals
def humanclick():
    timer=(uniform(0.01,0.015))
    time.sleep((timer/2) - 0.0005)
    pyautogui.mouseDown()
    time.sleep(timer)
    pyautogui.mouseUp()
    time.sleep((timer/2) - 0.0005)

#move to xy coordinate
def humanmovexy(x,y,safe='no',speed=3,sleep=0.0025):
    try:
        time.sleep(uniform(0.01,0.03))
        if (safe=='no'):
            overshoot(x,y)
        bezmouse.go((x,y),sleep=sleep,speed=speed)
        time.sleep(uniform(0.01,0.03))
    except:
        print("Move failed")
        return

def humanmoveobj(obj, safe='no',speed=3,sleep=0.0025):
    sleep = uniform(0.0018,0.0032)
    x = randint(obj[0], obj[0]+obj[2])
    y = randint(obj[1], obj[1]+obj[3])
    time.sleep(uniform(0.01,0.02))
    
    if safe=='no':
        overshoot(x,y)
        bezmouse.go((x,y),sleep=sleep,speed=speed)
    elif safe=='yes':
        bezmouse.go((x,y),deviation=10,speed=speed,sleep=sleep)
    time.sleep(uniform(0.01,0.03))