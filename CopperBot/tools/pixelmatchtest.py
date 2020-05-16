import cv2
import os
import pyautogui
from random import randint,uniform
from PIL import Image


dirname1 = os.path.dirname(os.path.abspath(__file__))
print(dirname1)
os.chdir(dirname1)



rgblist = (61, 31, 22), (47, 25, 15), (34, 17, 12), (50, 26, 17), (43, 22, 14), (30, 15, 10), (57, 30, 20), (39, 20, 14), (54,27,19)
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