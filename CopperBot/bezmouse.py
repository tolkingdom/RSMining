import pyautogui
import os, subprocess
from time import sleep
from random import randint, choice
from math import ceil
from multiprocessing import Process
import matplotlib.pyplot as plt
import cv2
import numpy
import time
from random import uniform

dirname1 = os.path.dirname(__file__)
os.chdir(dirname1)

pyautogui.MINIMUM_DURATION = 0.00
pyautogui.MINIMUM_SLEEP = 0.00
pyautogui.PAUSE = 0.00


    
def pascal_row(n):
    # This returns the nth row of Pascal's Triangle
    result = [1]
    x, numerator = 1, n
    for denominator in range(1, n//2+1):
        # print(numerator,denominator,x)
        x *= numerator
        x /= denominator
        result.append(x)
        numerator -= 1
    if n&1 == 0:
        # n is even
        result.extend(reversed(result[:-1]))
    else:
        result.extend(reversed(result)) 
    return result

  
def make_bezier(xys):

    # xys should be a sequence of 2-tuples (Bezier control points)
    n = len(xys)
    combinations = pascal_row(n - 1)
    def bezier(ts):
        # This uses the generalized formula for bezier curves
        # http://en.wikipedia.org/wiki/B%C3%A9zier_curve#Generalization
        result = []
        for t in ts:
            tpowers = (t**i for i in range(n))
            upowers = reversed([(1-t)**i for i in range(n)])
            coefs = [c*a*b for c, a, b in zip(combinations, tpowers, upowers)]
            result.append(
                list(sum([coef*p for coef, p in zip(coefs, ps)]) for ps in zip(*xys)))
        return result
    return bezier


def connected_bez(coord_list, deviation, speed):

    '''
    Connects all the coords in coord_list with bezier curve
    and returns all the points in new curve
    
    ARGUMENT: DEVIATION (INT)
        deviation controls how straight the lines drawn my the cursor
        are. Zero deviation gives straight lines
        Accuracy is a percentage of the displacement of the mouse from point A to
        B, which is given as maximum control point deviation.
        Naturally, deviation of 10 (10%) gives maximum control point deviation
        of 10% of magnitude of displacement of mouse from point A to B, 
        and a minimum of 5% (deviation / 2)
    '''
    
    points = []
    i = 1
    while i < len(coord_list):
        points += mouse_bez(coord_list[i - 1], coord_list[i], deviation, speed)
        i+=1
    return points


def mouse_bez(init_pos, fin_pos, deviation, speed):
    '''
    GENERATE BEZIER CURVE POINTS
    Takes init_pos and fin_pos as a 2-tuple representing xy coordinates
        variation is a 2-tuple representing the
        max distance from fin_pos of control point for x and y respectively
        speed is an int multiplier for speed. The lower, the faster. 1 is fastest.
            
    '''

    #time parameter
    ts = [t/(speed * 100.0) for t in range(speed * 101)]
    
    #bezier centre control points between (deviation / 2) and (deviaion) of travel distance, plus or minus at random
    control_1 = (init_pos[0] + choice((-1, 1)) * abs(ceil(fin_pos[0]) - ceil(init_pos[0])) * 0.01 * randint(deviation / 2, deviation),
                init_pos[1] + choice((-1, 1)) * abs(ceil(fin_pos[1]) - ceil(init_pos[1])) * 0.01 * randint(deviation / 2, deviation)
                    )
    control_2 = (init_pos[0] + choice((-1, 1)) * abs(ceil(fin_pos[0]) - ceil(init_pos[0])) * 0.01 * randint(deviation / 2, deviation),
                init_pos[1] + choice((-1, 1)) * abs(ceil(fin_pos[1]) - ceil(init_pos[1])) * 0.01 * randint(deviation / 2, deviation)
                    )
        
    xys = [init_pos, control_1, control_2, fin_pos]
    bezier = make_bezier(xys)
    points = bezier(ts)

    return points


# for i in range(4):
#     t = mouse_bez((1000,1000),(1600,700),30,10)
#     x = []
#     y = []
#     for i in t:
#         x.append(i[0])
#         y.append(i[1])
    
#     # plt.plot(x,y,'r')
#     # plt.xlim([0, 1920])
#     # plt.ylim([1080, 0 ])
#     # plt.show()   

# xlist = []
# ylist = []

# threshold = 0.8
# image = cv2.imread("img/beztest.png")
# template = cv2.imread("img/ironitem.png") 
# h,w,ch = template.shape
# result = cv2.matchTemplate(image,template,cv2.TM_CCOEFF_NORMED) 
# locations = numpy.where(result >= threshold)
# locations = list(zip(*locations[::-1]))
# # cv2.imshow('s',result)
# # cv2.waitKey()
# print(locations)
# for i in locations:
#     x,y =  i

# for i in connected_bez(locations,100,3):
#     xlist.append(i[0])
#     ylist.append(i[1])

# plt.plot(xlist,ylist,'r')
# plt.xlim([0, 237])
# plt.ylim([340, 0 ])
# plt.show()  

# XY = list(zip(xlist,ylist))
# for pos in XY:
#     pyautogui.moveTo(pos)
#     time.sleep(0.0)


def go(destxy,deviation=50,speed=3,sleep=0.0025):
    startxy = pyautogui.position()
    path = mouse_bez(startxy,destxy,deviation,speed)
    for i in path:
        pyautogui.moveTo(i)
        time.sleep(sleep)

# go((600,600),deviation=2)
# go((900,300),deviation=2)
# go((300,900),deviation=2)