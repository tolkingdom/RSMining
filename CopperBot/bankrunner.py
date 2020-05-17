import pyautogui
from random import uniform,randint
import bezmouse
import os

dirname1 = os.path.dirname(os.path.abspath(__file__))
print(dirname1)
os.chdir(dirname1)


#defining global variables and determining mouse coordinates
x0,y0 = calibrate()
bottomright = x0+765,y0+502
client=(x0,y0,765,502)
textnotif=(x0+3,y0+440,400,25)
gamewindow=(x0+5,y0+4,515,334)
inventory=(x0+549,y0+210,183,253)
motionbox=(x0+300,y0,45,45)
mapbox=(x0+568,y0+11,151,151)
bankdep = (228,83,83),(227,82,82)

#MAIN LOOP
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


def matchtooltip(image):
    cx,cy = pyautogui.position()
    box = (cx-120,xy-75,240,150)  
    return len(imgmatchscreenall(image,region1=box))>0

def overshoot(x,y):
    sleep = uniform(0.0018,0.0032)
    if randint(0,10)>=3:
        return 
    currentx,currenty = pyautogui.position()
    if currentx<=x:
        xdir = 1
    else:
        xdir = -1
    if currenty<=y:
        ydir = 1
    else:
        ydir = -1
    x2=randint(10,25)
    y2=randint(10,25)
    bezmouse.go(((xdir*x2)+x,(ydir*y2)+y),sleep=sleep)

def randomcameramove(steps,honly='no'):
    for i in range (steps):
        key = randint(1,4)
        if honly=='yes':
            key = randint(1,2)
        delay = uniform(0.005,0.01)
        hold = uniform(0.1,1.0)
        if key == 1:
            print('pressing left')
            pyautogui.keyDown('left')
            time.sleep(hold)
            pyautogui.keyUp('left')
            time.sleep(delay)
        if key == 2:
            print('pressing right')            
            pyautogui.keyDown('right')
            time.sleep(hold)
            pyautogui.keyUp('right')
            time.sleep(delay)
        if key == 3:
            print('pressing up')            
            pyautogui.keyDown('up')
            time.sleep(hold)
            pyautogui.keyUp('up')
            time.sleep(delay)
        if key == 4:
            print('pressing down')
            pyautogui.keyDown('down')
            time.sleep(hold)
            pyautogui.keyUp('down')
            time.sleep(delay)

def checkstats():
    rando = uniform(1.1,3.2)
    stat = imgmatchscreen("img/statbar.png", region1=client)
    humanmoveobj(stat)
    humanclick()
    minestat = imgmatchscreen("img/miningstat.png", region1=client,)
    humanmoveobj(minestat)
    time.sleep(rando)
    bag = imgmatchscreen("img/bag.png", region1=client)
    humanmoveobj(bag)
    humanclick()

def checkrun():
    if len(list(imgmatchscreenall('img/fullrun.png',region1=(client))))>0:
        humanmoveobj(imgmatchscreen('img/fullrun.png',region1=(client),threshold=0.6))
        humanclick()


