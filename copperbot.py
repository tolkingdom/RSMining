import subprocess
import cv2
import pyautogui
from random import randint,uniform
import time
import pyscreeze
import math
import numpy
import datetime
import humanmouse
from PIL import Image


def mine(oretype,queuexy=None):
    global failedCount
    print("starting mine")
    global qxy
    global oldmousepos
    orig = orecount(oretype)
    if (qxy==None):
        x,y = colormatch(oretype)
    else:
        x,y = qxy
    statcheck=randint(1,50)
    #while oldmousepos[0]-40 <= x <= oldmospos[0]+40
    if pyautogui.position() != (x,y):
        humanmovexy(x,y)
    qxy = None
    xtest,ytest = pyautogui.position()
    if len(list(pyautogui.locateAllOnScreen('img/minerocks.png',confidence=0.50,region=(gamewindow[0],gamewindow[1],100,100)))) > 0:
        humanclick()
        oldmousepos = pyautogui.position()
        time.sleep(uniform(0.100,0.130))
        attempts1=0
        while len(list(pyautogui.locateAllOnScreen('img/swing.png',confidence=0.85,region=(textnotif)))) == 0 and (attempts1!=100): 
            if len(list(pyautogui.locateAllOnScreen('img/noore.png',confidence=0.85,region=(textnotif)))) > 0:
                print("no ore here, retarting mine")
                failedCount+=1
                print("Failed count is at " + str(failedCount))
                return
            attempts1+=1
            time.sleep(0.05)
    else:
        return
    attempts = 0
    if qxy == None:
        qxy = colormatch(oretype,move="yes")
        humanmovexy(qxy[0],qxy[1])
    if statcheck==5:
        checkstats()
        attempts+=10
    while orecount(oretype) == orig and attempts<=20:
        print("waiting on ore to mine")
        time.sleep(0.5)
        attempts+=1



    if failedCount>0:
        failedCount-=1


def colormatch(oretype,move="no"):
    print("starting color match")
    if oretype == "copper":
        rgblist = (113,73,41),(91,59,33),(82,53,29),(79,50,27),(129,83,46),(101, 65, 35),(95, 61, 34),(75, 48, 26),(69, 44, 25),(72, 47, 25)
        #img = pyautogui.screenshot(region=gamewindow)
        #pixel = pyautogui.pixel(1,1)
    elif oretype == "iron":
        rgblist = (64, 34, 23), (61, 31, 22), (47, 25, 15), (34, 17, 12), (50, 26, 17), (43, 22, 14), (30, 15, 10), (57, 30, 20), (26, 14, 9), (39, 20, 14), (54,27,19)
    
    im = pyautogui.screenshot(region=gamewindow)
    pimpg = im.load()
    w,h = im.size
    for k in range(0,(w*h)):
        x = randint(0,w-1)
        y = randint(0,h-1)
        for i in rgblist:
            if pimpg[x,y] == i:
                print("found match at: " + str(x)+" "+str(y))
                x=x+gamewindow[0]
                y=y+gamewindow[1]
                print (x,y)
                return x,y


def drop(oretype):
    try:
        if oretype == "copper":
            l = list(pyautogui.locateAllOnScreen('img/copperitem.png',confidence=.90,region=(inventory)))
            for i in l:
                humanmoveobj(i,safe='yes')
                humanrclick()
                try:
                    humanmoveobj(pyautogui.locateOnScreen('img/dropcop.png',confidence=0.95,region=(client)),safe='yes')
                except:
                    humanmoveobj(pyautogui.locateOnScreen('img/dropyellow.png',confidence=0.95,region=(client)),safe=yes)                
                humanclick()
        if oretype == "iron":
            l = list(pyautogui.locateAllOnScreen('img/ironitem.png',confidence=.90,region=(inventory)))
            for i in l:
                humanmoveobj(i,safe='yes')
                humanrclick()
                try:
                    humanmoveobj(pyautogui.locateOnScreen('img/dropiron.png',confidence=0.95,region=(client)),safe='yes')
                except:
                    humanmoveobj(pyautogui.locateOnScreen('img/dropyellow.png',confidence=0.95,region=(client)),safe='yes')                
                humanclick()
    except: 
        return

def worldhop():
    print("Hopping worlds")
    pyautogui.hotkey("ctrl","shift","right")
    time.sleep(10.0)
    pyautogui.press("esc")

def nospace():
    print("no inv space left")
    return len(list(pyautogui.locateAllOnScreen('img/space.png',confidence=.50,region=(inventory)))) ==0

def isfull(oretype):
    return (orecount(oretype)>=24)


def orecount(oretype):
    if oretype == "copper":
        return len(list(pyautogui.locateAllOnScreen('img/copperitem.png',confidence=.70,region=(inventory))))
    if oretype == "iron":
        return len(list(pyautogui.locateAllOnScreen('img/ironitem.png',confidence=.70,region=(inventory))))
    else:
        return 0


def checkstats():
    rando = uniform(1.1,3.2)
    stat = pyautogui.locateOnScreen("img/statbar.png", region=client, confidence=0.75)
    humanmoveobj(stat,safe='yes')
    humanclick()
    minestat = pyautogui.locateOnScreen("img/miningstat.png", region=client, confidence=0.60)
    humanmoveobj(minestat)
    time.sleep(rando)
    bag = pyautogui.locateOnScreen("img/bag.png", region=client, confidence=0.75)
    humanmoveobj(bag)
    humanclick()



def randomcameramove():
    steps = randint(1,5)
    for i in range (steps):
        key = randint(1,4)
        delay = uniform(0.005,0.01)
        hold = uniform(0.3,0.9)
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

def humanmoveobj(obj, safe='no'):
    speed = uniform(0.2,0.5)
    x = randint(obj[0], obj[0]+obj[2])
    y = randint(obj[1], obj[1]+obj[3])
    time.sleep(uniform(0.05,0.08))
    
    if safe=='no':
        humanmouse.go((x,y),speed)
    elif safe=='yes':
        humanmouse.go((x,y),speed,safe='yes')
    time.sleep(uniform(0.05,0.15))


def humanmovexy(x,y):
    speed = uniform(0.5,1.3)
    humanmouse.go((x,y),speed)
    time.sleep(uniform(0.05,0.08))


def humanclick():
    timer=(uniform(0.01,0.015))
    time.sleep((timer/2) - 0.0005)
    pyautogui.mouseDown()
    time.sleep(timer)
    print("slept for " + str(timer))
    pyautogui.mouseUp()
    #time.sleep((timer/2) - 0.0009)
    
def humanrclick():
    timer=(uniform(0.01,0.015))
    time.sleep((timer/2) - 0.00005)
    pyautogui.mouseDown(button='right')
    time.sleep(timer)
    print("slept for " + str(timer))
    pyautogui.mouseUp(button='right')
    time.sleep((timer/2) - 0.00009)

def calibrate():
    l,t,w,h = pyautogui.locateOnScreen("img/runelite.png")
    print (l,t,w,h)
    return l,t+27

def convertxy(x,y):
    x2=x-x0
    y2=y-y0
    print(x2,y2)
    return x2,y2


qxy = None
failedCount = 0
x0,y0 = calibrate()
print(x0,y0)
oldmousepos = (x0,y0)
bottomright = x0+765,y0+502
client=(x0,y0,765,502)
textnotif=(x0+3,y0+440,236,25)
gamewindow=(x0+5,y0+4,515,334)
inventory=(x0+549,y0+210,183,253)
oretype = "iron" #pyautogui.prompt("Ore Select 'copper' or 'iron'")
print(oretype=="iron")
print(oretype)
print(inventory)
pyautogui.screenshot(imageFilename="inventory.png", region=(inventory))
pyautogui.screenshot(imageFilename="client.png", region=(client))
pyautogui.screenshot(imageFilename="gamewindow.png", region=(gamewindow))
pyautogui.screenshot(imageFilename="inventory.png", region=(inventory))
pyautogui.screenshot(imageFilename="client.png", region=(client))
pyautogui.screenshot(imageFilename="texnotif.png", region=(textnotif))
print(x0,y0)


start_time = time.time()
while True:
    odds=randint(1,100)
    now = round(time.time() - start_time)
    print(str(now/60) + 'minutes of runtime' )
    if (isfull(oretype) or nospace()):
        print("full")
        drop(oretype)    
    if odds <= 20:
        qxy = None
        randomcameramove()
    if failedCount >= 10:
        worldhop()
        failedCount = 0
    if (isfull(oretype) == False):
        #print("not full")
        #print(coppercount())
        mine(oretype,queuexy= qxy)
