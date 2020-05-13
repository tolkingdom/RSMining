import numpy as np
import matplotlib.pyplot as plt
from math import sqrt
from random import randint,uniform
import pyautogui
import time

def construct_path(points):
    x = points[:,0]
    y = points[:,1]

    (x_new,y_new) = ([],[])
    for i in range(0,len(x) - 2):
        (x_tmp, y_tmp) =  get_new_points(x[i:(i+3)], y[i:(i+3)], (i+3) == len(x))
        (x_new,y_new) = (x_new + x_tmp.tolist(), y_new + y_tmp.tolist())
        previous_points = [x_tmp,y_tmp]
    xfin = [round(t) for t in x_new]
    yfin = [round(t) for t in y_new]

    return (xfin),(yfin)

def get_new_points(x,y, end):
    x = np.array(x)
    y = np.array(y)

    # calculate polynomial
    z = np.polyfit(x, y, 2)
    f = np.poly1d(z)

    # calculate new x's and y's

    if not end:
        x_new = np.linspace(x[0], x[1], 11)
    else:
        x_new = np.linspace(x[0], x[1], 10, endpoint=False).tolist() + np.linspace(x[1], x[2], 11).tolist()
        x_new = np.array(x_new)
    y_new = f(x_new)

    
    return (x_new, y_new)




def go(destxy,duration=0.2,safe='no'):
    startxy = pyautogui.position()
    dst = int(sqrt((abs(startxy[0]-destxy[0]))*(abs(startxy[0]-destxy[0]))+(abs(startxy[1]-destxy[1]))*(abs(startxy[1]-destxy[1]))))
    print(dst)
    #destxy = (1600,400) sqrt()
    #startxy =(273,920)
    if safe == 'no':
        windowxy = (int((destxy[0]+startxy[0])/2), int((destxy[1]+startxy[1])/2))
        rdm1 = randint(-(int(dst/4.5)),int((dst/4.5)))
        rdm2 = randint(-(int(dst/4.5)),int((dst/4.5)))
        print(rdm1,rdm2)
    elif safe == 'yes':
        #windowxy = (int(1.5*((destxy[0]+startxy[0])/2)), int(1.5*((destxy[1]+startxy[1])/2)))
        windowxy = (int((destxy[0]+startxy[0])/2), int((destxy[1]+startxy[1])/2))
        rdm1 = randint(-(int(dst/25)),int((dst/25)))
        rdm2 = randint(-(int(dst/25)),int((dst/25)))
        print(rdm1,rdm2)
    randomxy = windowxy[0]+rdm1,windowxy[1]+rdm2
    points = np.array([startxy,randomxy,destxy])
    x = points[:,0]
    y = points[:,1]
    ( x_new, y_new) = construct_path(points)
    XY = list(zip(x_new,y_new))
    #plt.plot(x,y,'o',np.array(x_new),np.array(y_new))
    #plt.xlim([0, 1920])
    #plt.ylim([1080, 0])
    #plt.show()
    step = 1 / len (XY)
    timeout = duration / len(XY)
    pyautogui.MINIMUM_DURATION = 0
    pyautogui.MINIMUM_SLEEP = 0
    pyautogui.PAUSE = 0
    for pos in XY:
        pyautogui.moveTo(pos)
        time.sleep(timeout*uniform(0.8,1.2))

def model(startxy,destxy,duration=0.2,safe='no'):
    dst = int(sqrt((abs(startxy[0]-destxy[0]))*(abs(startxy[0]-destxy[0]))+(abs(startxy[1]-destxy[1]))*(abs(startxy[1]-destxy[1]))))
    print(dst)
    #destxy = (1600,400) sqrt()
    #startxy =(273,920)
    if safe == 'no':
        windowxy = (int((destxy[0]+startxy[0])/2), int((destxy[1]+startxy[1])/2))
        rdm1 = randint(-(int(dst/4.5)),int((dst/4.5)))
        rdm2 = randint(-(int(dst/4.5)),int((dst/4.5)))
        print(rdm1,rdm2)
    elif safe == 'yes':
        windowxy = (int(((destxy[0]+startxy[0])/2)), int(((destxy[1]+startxy[1])/2)))
        #windowxy = (int((destxy[0]+windowxy[0])/2), int((destxy[1]+windowxy[1])/2))
        rdm1 = randint(-(int(dst/20)),int((dst/20)))
        rdm2 = randint(-(int(dst/20)),int((dst/20)))
        print(rdm1,rdm2)
    randomxy = windowxy[0]+rdm1,windowxy[1]+rdm2
    points = np.array([startxy,randomxy,destxy])
    x = points[:,0]
    y = points[:,1]
    (  x_new, y_new) = construct_path(points)
    XY = list(zip(x_new,y_new))
    plt.plot(x,y,'o',np.array(x_new),np.array(y_new))
    plt.xlim([0, 1920])
    plt.ylim([1080, 0])
    plt.show()   

#for i in range(5):
    #model((345,200),(295,800),safe='no')