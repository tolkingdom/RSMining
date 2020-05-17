import subprocess
import cv2
import pyautogui
from random import randint,uniform
import time
import pyscreeze
import math
import numpy 
import datetime
import bezmouse
import os

from pathlib import Path
from PIL import Image

dirname1 = os.path.dirname(os.path.abspath(__file__))
print(dirname1)
os.chdir(dirname1)

def mine(oretype):
    global qxy
    global failedCount
    clicked=False
    statrand = randint(1,100)
    print("Starting Mine")
    # if qxy == None:
    #     qxy = colormatch(oretype)
    # if pyautogui.position != qxy:
    #     humanmovexy(qxy[0],qxy[1])
    oldcount = orecount(oretype)
    if len(list(imgmatchscreenall('img/minerocks.png',region1=(client),threshold=0.60))) > 0:
        if greycursor() == False:
            humanclick()
            clicked=True
            time.sleep(uniform(0.005,0.02))
            if statrand>=95:
                randomcameramove(randint(1,2),honly='yes')
        else:
            qxy=None
           
    else:
        qxy = None
    if statrand==50:
        time.sleep(uniform(0.0100,0.0400))
        checkstats()
        return
    
    # while inMotion():
    #     print("Moving")
    increment=0
    #while len(list(imgmatchscreenall('img/swing.png',region1=(textnotif),threshold=0.50))) == 0 and orecount(oretype)==oldcount and increment <=20 and clicked : 
        #increment+=1
        #time.sleep(0.01)
    #if increment >= 20:
        #failedCount+=1
        #print("failcount incremeted to "+str(failedCount))
        #return

    oldx,oldy = pyautogui.position()
    newx,newy = oldx,oldy
    increment=0
    try:
        while oldx-55<newx<oldx+55 or oldy-40<newy<oldy+55 and increment!=55:
            qxy = colormatch(oretype)
            newx,newy = qxy
            increment+=1
    except:
        print("No iron on screen")
    try:
        humanmovexy(qxy[0],qxy[1])

    except:
        print("move failed during mine")
    increment=0
    while orecount(oretype) == oldcount and increment <= 25  and clicked:
        print("Waiting for ore")
        increment+=1
        time.sleep(0.025)
    if increment >= 25:
        failedCount+=1
        print("failcount incremeted to "+str(failedCount))
    
    return
            



def colormatch(oretype='iron',move="no",inputlist=None):
    try:
        print("starting color match")
        
        if oretype == "copper":
            rgblist = (113,73,41),(91,59,33),(82,53,29),(79,50,27),(129,83,46),(101, 65, 35),(95, 61, 34),(75, 48, 26),(69, 44, 25),(72, 47, 25)
            #img = pyautogui.screenshot(region=gamewindow)
            #pixel = pyautogui.pixel(1,1)
        elif oretype == "iron":
            rgblist = (64, 34, 23), (61, 31, 22), (47, 25, 15), (34, 17, 12), (50, 26, 17), (43, 22, 14), (30, 15, 10), (57, 30, 20), (26, 14, 9), (39, 20, 14), (54,27,19)
        if inputlist != None: 
            rgblist = inputlist
        im = pyautogui.screenshot(region=gamewindow)
        
        pimpg = im.load()
        w,h = im.size
        for k in range(0,(w*h)):
            x = randint(0,w-1)
            y = randint(0,h-1)
            for i in rgblist:
                if pimpg[x,y] == i:
                    x=x+gamewindow[0]
                    y=y+gamewindow[1]
                    return x,y
    except:
        print("No color found")
        return None

# def pixelmap(pixlist,tolerance=30):
#     im = pyautogui.screenshot(region=mapbox)
#     pimpg = im.load()
#     w,h = im.size
#     for k in range(0,(w*h)):
#         x = randint(0,w-1)
#         y = randint(0,h-1)
#         for i in pixlist:
#             exR,exG,exB = i[0],i[1],i[2]
#         r,g,b = pimpg[x,y]       
#         if (abs(r - exR) <= tolerance) and (abs(g - exG) <= tolerance) and (abs(b - exB) <= tolerance):
#             return x+mapbox[0],y+mapbox[1]


# pyautogui.pixelMatchesColor
def imgmatchscreen(small, region1=None, threshold=0.7):
    max_val=0.0
    counter=0
    print("starting img match loop")
    while max_val <= threshold and counter<=250:
        ssht = pyautogui.screenshot(imageFilename=None, region=region1)
        img = numpy.array(ssht)
        image = img[:, :, ::-1].copy()
        template = cv2.imread(small,cv2.IMREAD_COLOR) 
        h,w,ch = template.shape
        result = cv2.matchTemplate(image,template,cv2.TM_CCOEFF_NORMED)  
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        x,y = max_loc
        counter+=1
    print("max val for this match was "+str(max_val))
    if region1!=None:
        x0,y0 = region1[:2]
        x=x+x0
        y=y+y0
    imgbox = x,y,w-1,h-1
    print ("returning" + str(imgbox))
    return imgbox


def imgmatchscreenall(small, region1=None, threshold=0.6):
    locbox = []
    img = numpy.array(pyautogui.screenshot(region=region1))
    image = img[:, :, ::-1].copy()
    template = cv2.imread(small) 
    h,w,ch = template.shape
    result = cv2.matchTemplate(image,template,cv2.TM_CCOEFF_NORMED) 
    locations = numpy.where(result >= threshold)
    locations = list(zip(*locations[::-1]))
    #print(len(locations))
    for i in locations:
        #print(i)
        x,y =  i
        if region1!=None:
            x0,y0 = region1[:2]
            x=x+x0
            y=y+y0
        locbox.append((x,y,w-1,h-1))
    return locbox

def bank(skiphalf='no'):
    print("Starting BANK run")
    humanzoomout()
    print("Looking for ladder")
    while matchtooltip('img/ladder.png') == False:
        try:
            x,y = colormatch(inputlist=(239,104,104))
            humanmovexy(x,y)
        except:
            a = None
    print("Found ladder, clicking")
    time.sleep(uniform(0.05,0.08))    
    humanclick()
    time.sleep(uniform(0.5,1.5))
    print("Looking for bank booth")
    while matchtooltip('img/bankbooth.png') == False:
        x,y = colormatch(inputlist=((239,104,104),(238,103,103))
        humanmovexy(x,y)
    print("Found bank booth, clicking")
    time.sleep(uniform(0.05,0.08)) 
    humanclick()
    time.sleep(uniform(3,5))
    print("Waiting until bank is open")
    while len(list(imgmatchscreenall('img/inbank.png',region1=(gamewindow),threshold=0.60))) == 0:
        time.sleep(0.33)
    print("Inside Bank, clicking all iron ore and gems")
    iron = imgmatchscreen('img/ironitem.png',region1=(inventory))
    ruby = imgmatchscreen('img/ruby.png',region1=(inventory))
    sapphire = imgmatchscreen('img/sapphire.png',region1=(inventory))
    emerald = imgmatchscreen('img/emerald.png',region1=(inventory))
    diamond = imgmatchscreen('img/diamond.png',region1=(inventory))
    items = (iron,ruby,sapphire,emerald,diamond)
    for i in items:
        time.sleep(uniform(0.05,0.1))
        humanmoveobj(i,safe='yes')
        time.sleep(uniform(0.05,0.08))
        humanclick()
    print("Items deposited, clicking X")
    closebank = imgmatchscreen('img/bankx.png',region1=gamewindow)
    humanmoveobj(closebank, safe='yes')
    time.sleep(uniform(0.05,0.08))
    humanclick()
    print("Looking for ladder")
    while matchtooltip('img/ladder.png') == False:
        x,y = colormatch(inputlist=(250,0,255))
        humanmovexy(x,y)
    print("Found ladder, clicking")
    time.sleep(uniform(0.05,0.08))
    humanclick()
    time.sleep(uniform(0.5,1.5))
    print("Looking for Ore!")
    while matchtooltip('img/minerocks.png') == False:
        x,y = colormatch(inputlist=(250,0,255))
        humanmovexy(x,y)
    print("Found Ore, clicking and Zooming IN")
    time.sleep(uniform(0.05,0.08))
    humanclick()
    time.sleep(uniform(3,5))
    humanzoomin()



    # increment = 0
    # humanmoveobj((x0+555,y0+15,15,15),safe='yes')
    # time.sleep(uniform(0.1,0.2))
    # humanclick()
    # zero = "img/0.png"
    # one = "img/1.png"
    # two = "img/2.png"
    # three = "img/3.png"
    # four = "img/4.png"
    # five = "img/5.png"
    # six = "img/6.png"
    # seven ="img/7.png"
    # bankdep = (228,83,83),(227,82,82)
    # listoflist = [zero,one,two,three,four,five,six,seven]
    # if skiphalf == 'no':
    #     for pos,i in enumerate(listoflist):

    #         time.sleep(0.1)
    #         a,b,c,d = imgmatchscreen(i,region1=mapbox,threshold=0.7)
    #         humanmovexy(a+randint(-2,2),b+randint(-2,2),safe='yes')
    #         humanclick()
    #         time.sleep(1.0)
    #         # while inMotion() and increment<=400:
    #         #     time.sleep(0.1)
    #         if i != listoflist[-1]:
    #             imgmatchscreen(listoflist[pos+1],region1=mapbox,threshold=0.97)
            
    #         increment = 0
    #     checkrun()
    #     while((colormatch(inputlist=bankdep) == None) or inMotion()):
    #         randomcameramove(1)
    #         time.sleep(0.1)
        
        
    #     pyautogui.keyDown('up')
    #     time.sleep(uniform(1.5,2.1))
    #     pyautogui.keyUp('up')
    #     try:
    #         humanmoveobj(imgmatchscreen("img/ironitem.png",inventory))
    #         time.sleep(uniform(0.05,0.1))
    #         humanclick()
    #         humanmovexy(colormatch(inputlist=bankdep)[0],colormatch(inputlist=bankdep)[1])
    #         humanclick()
    #         time.sleep(uniform(3.0,3.5))
    #         humanmoveobj(imgmatchscreen("img/bankall.png",client),safe='yes')
    #         humanclick()
    #         humanmoveobj((x0+555,y0+15,15,15),safe='yes')
    #         time.sleep(uniform(0.1,0.2))
    #         humanclick()
    #     except:
    #         print("bank failed")

    
    # for pos,i in enumerate(reversed(listoflist)):
    #     print(i)
    #     time.sleep(0.1)
    #     a,b,c,d = imgmatchscreen(i,region1=mapbox,threshold=0.7)
    #     humanmovexy(randint(a,a+c),randint(b,b+d),safe='yes')
    #     humanclick()
    #     time.sleep(1.0)
    #     increment = 0
    #     # while inMotion() and increment<=400:
    #     #     time.sleep(0.5)
    #     if i != listoflist[0]:
    #         print(listoflist[-(pos+1)])
    #         imgmatchscreen(listoflist[-(pos+1)],region1=mapbox,threshold=0.95)
    #         time.sleep(6.0)
    #     increment = 0
    # if colormatch(oretype) == None:
    #     bank(skiphalf='yes')

   # zero = (219, 19, 177), (247, 3, 192), (172, 31, 106), (130, 47, 58), (221, 18, 179), (247, 3, 195), (213, 15, 171), (180, 41, 150), (180, 41, 151), (216, 15, 156), (218, 14, 159)
    # one = (151, 3, 243), (139, 14, 197), (122, 30, 133), (140, 13, 200), (106, 45, 72), (106, 45, 71), (140, 13, 201), (138, 13, 196), (120, 28, 133), (139, 12, 201)
    # two = (65, 23, 202), (62, 76, 78), (63, 50, 138), (67, 5, 244), (65, 24, 199), (66, 22, 203), (64, 50, 139)
    # three = (227, 19, 183), (201, 29, 163), (202, 30, 163), (199, 30, 162), (160, 46, 133), (228, 20, 179), (204, 34, 146)
    # four = (151, 3, 243), (139, 14, 197), (122, 30, 133), (140, 13, 200), (106, 45, 72), (106, 45, 71), (140, 13, 201), (138, 13, 196), (120, 28, 133), (139, 12, 201)
    # five = (219, 19, 177), (247, 3, 192), (172, 31, 106), (130, 47, 58), (221, 18, 179), (247, 3, 195), (213, 15, 171), (180, 41, 150), (180, 41, 151), (216, 15, 156), (218, 14, 159)
    # bankdep = (228,83,83)
    # listoflist = [zero,one,two,three,four,five]
    # for i in listoflist:
    #     while pixelmap(i) == None:
    #         randomcameramove(1)
    #         time.sleep(0.01)
    #     x,y = pixelmap(i)
    #     humanmovexy(x,y)
    #     humanclick()
    #     time.sleep(1.0)
    #     while inMotion():
    #         time.sleep(0.1)

    # for i in reversed(listoflist):
    #     while pixelmap(i) == None:
    #         randomcameramove(1)
    #         time.sleep(0.01)
    #     x,y = pixelmap(i)
    #     humanmovexy(x,y)
    #     humanclick()
    #     time.sleep(1.0)
    #     while inMotion():
    #         time.sleep(0.1)
    
    


def drop(oretype):
    try:
        if oretype == "copper":
            l = list(imgmatchscreenall('img/copperitem.png',region1=(inventory)))
            for i in l:
                humanmoveobj(i,safe='yes')
                humanrclick()
                try:
                    humanmoveobj(imgmatchscreenall('img/dropcop.png',region1=(client)),safe='yes')
                except:
                    humanmoveobj(imgmatchscreen('img/dropyellow.png',region1=(client)),safe=yes)                
                humanclick()
        if oretype == "iron":
            l = list(imgmatchscreenall('img/ironitem.png',region1=(inventory)))
            for i in l:
                pyautogui.keyDown('shift')
                time.sleep(uniform(0.01,0.015))
                humanmoveobj(i,safe='yes',speed=1,sleep=0.002)        
                humanclick()
                time.sleep(uniform(0.01,0.015))
                pyautogui.keyUp('shift')
    except: 
        return


def inMotion():
    box = motionbox
    past = pyautogui.screenshot(region=box)
    time.sleep(0.1)
    present = pyautogui.screenshot(region=box)
    if past==present:
        return False
    else:
        return True

def greycursor():
    greylist = (67,61,61), (64, 59, 59), (50, 46, 46), (42, 38, 38), (34, 30, 30), (29, 26, 26), (47, 43, 43), (44, 41, 41), (25, 23, 23), (37, 33, 33), (39, 35, 35), (57, 52, 52), (62, 56, 56), (60, 54, 54), (53, 48, 47), (55, 49, 49), (31, 27, 27), (22, 20, 20), (9, 7, 7), (12, 10, 10), (15, 14, 14), (19, 17, 17)
    sx,sy = pyautogui.position()
    box = (sx-5,sy-5,10,10)
    im = pyautogui.screenshot(region=box)
    pimpg = im.load()
    w,h = im.size
    for k in range(0,(w*h)):
        x = randint(0,w-1)
        y = randint(0,h-1)
        for i in greylist:
            if pimpg[x,y] == i:
                ("FOUND GREY BEFORE CLICK")
                return True
    return False

def worldhop():
    print("Hopping worlds")
    pyautogui.hotkey("ctrl","shift","right")
    time.sleep(10.0)
    pyautogui.press("esc")

def nospace():
    return len(list(imgmatchscreenall('img/space.png',region1=(inventory),threshold=.45))) ==0

def isfull(oretype):
    return (orecount(oretype)>=27)


def orecount(oretype):
    if oretype == "copper":
        return len(list(imgmatchscreenall('img/copperitem.png',region1=(inventory))))
    if oretype == "iron":
        return len(list(imgmatchscreenall('img/ironitem.png',region1=(inventory))))
    else:
        return 0

 
    if len(list(imgmatchscreenall('img/fullrun.png',region1=(client))))>0:
        humanmoveobj(imgmatchscreen('img/fullrun.png',region1=(client),threshold=0.6))
        humanclick()

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
        time.sleep(uniform(0.05,0.08))
        humanclick()


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

def humanzoomout():
    for i in range(1,4):
        pyautogui.scroll(-12)
        time.sleep(uniform(0.02,0.35))

def humanzoomin():
    for i in range(1,5):
        pyautogui.scroll(12)
        time.sleep(uniform(0.02,0.35))

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


def humanmovexy(x,y,safe='no',speed=3,sleep=0.0025):
    try:
        if (safe=='no'):
            overshoot(x,y)
        sleep = uniform(0.0010,0.0025)
        bezmouse.go((x,y),sleep=sleep,speed=speed)
        time.sleep(uniform(0.01,0.03))
    except:
        print("Move failed")
        return

def humanclick():
    timer=(uniform(0.01,0.015))
    time.sleep((timer/2) - 0.0005)
    pyautogui.mouseDown()
    time.sleep(timer)
    pyautogui.mouseUp()
    #time.sleep((timer/2) - 0.0009)
    
def humanrclick():
    timer=(uniform(0.005,0.015))
    time.sleep((timer/2) - 0.00005)
    pyautogui.mouseDown(button='right')
    time.sleep(timer)
    pyautogui.mouseUp(button='right')
    time.sleep((timer/2) - 0.00009)

def calibrate():
    l,t,w,h = imgmatchscreen('img/runelite.png')
    print ("calibrated to : " + str((l,t,w,h)))
    return l,t+27

def convertxy(x,y):
    x2=x-x0
    y2=y-y0
    print(x2,y2)
    return x2,y2

def matchtooltip(image):
    cx,cy = pyautogui.position()
    box = (cx-120,cy-75,240,150)  
    return len(imgmatchscreenall(image,region1=box))>0


qxy = None
failedCount = 0
x0,y0 = calibrate()
print("Calibrated to game window at: " + str((x0,y0)))
oldmousepos = (x0,y0)
bottomright = x0+765,y0+502
client=(x0,y0,765,502)
textnotif=(x0+3,y0+440,236,25)
gamewindow=(x0+5,y0+4,515,334)
inventory=(x0+549,y0+210,183,253)
motionbox=(x0+300,y0,45,45)
mapbox=(x0+568,y0+11,151,151)
bankdep = (228,83,83),(227,82,82)
oretype = "iron" #pyautogui.prompt("Ore Select 'copper' or 'iron'")
print("Selected ore: " + str(oretype))
pyautogui.screenshot(imageFilename="debug/inventory.png", region=(inventory))
pyautogui.screenshot(imageFilename="debug/client.png", region=(client))
pyautogui.screenshot(imageFilename="debug/gamewindow.png", region=(gamewindow))
pyautogui.screenshot(imageFilename="debug/inventory.png", region=(inventory))
pyautogui.screenshot(imageFilename="debug/client.png", region=(client))
pyautogui.screenshot(imageFilename="debug/texnotif.png", region=(textnotif))
pyautogui.screenshot(imageFilename="debug/mapbox.png", region=(mapbox))
print(x0,y0)


start_time = time.time()

#MAIN LOOP
while True:
    #bank()
    #checkrun()
    odds=randint(1,100)
    now = round(time.time() - start_time)
    print(str(now/60) + 'minutes of runtime' )
    if (isfull(oretype) or nospace()):
        print("full")
        #drop(oretype)
        checkrun()
        bank()
        failedCount = 0
    #if colormatch(inputlist=bankdep) != None:
        #bank(skiphalf='yes')
    if odds <= 10:
        qxy = None
        randomcameramove(randint(1,5),honly='yes')
    if failedCount >= 3:
        worldhop()
        failedCount = 0
    #if (isfull(oretype) == False):
        #print("not full")
        #print(coppercount())
    mine(oretype)

