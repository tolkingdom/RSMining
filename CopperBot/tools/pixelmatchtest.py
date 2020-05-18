import cv2
import os
import pyautogui
from random import randint,uniform
from PIL import Image


dirname1 = os.path.dirname(os.path.abspath(__file__))
print(dirname1)
os.chdir(dirname1)



rgblist = (47, 25, 15), (57, 30, 20), (48, 25, 16), (39, 20, 14), (50, 26, 17), (54, 27, 19), (34, 17, 12), (43, 22, 14), (31, 15, 10), (45, 23, 14), (54, 28, 19), (26, 14, 9), (59, 30, 21), (53, 27, 18)
im = Image.open('../gamewindow.png')
pimpg = im.load()
w,h = im.size
tolerance = 1  
for i in rgblist:
    counter = 0
    for x in range(w):
        for y in range(h):   
            if (pimpg[x,y] == i ):
                counter+=1
                pimpg[x,y] = (0,0,255)
    print (str(i)+ " had " + str(counter) + " matches")
im.show()