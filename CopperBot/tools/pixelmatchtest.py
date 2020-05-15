import cv2
import os
import pyautogui
from random import randint,uniform
from PIL import Image


dirname1 = os.path.dirname(os.path.abspath(__file__))
print(dirname1)
os.chdir(dirname1)



rgblist = (151, 3, 243), (139, 14, 197), (122, 30, 133), (140, 13, 200), (106, 45, 72), (106, 45, 71), (140, 13, 201), (138, 13, 196), (120, 28, 133), (139, 12, 201)
im = Image.open('../worldmap/4.png')
pimpg = im.load()
w,h = im.size
tolerance = 20
for k in range(0,(w*h)):
    x = randint(0,w-1)
    y = randint(0,h-1)
    for i in rgblist:
        exR,exG,exB = i[0],i[1],i[2]
        r,g,b,a = pimpg[x,y]       
        if (abs(r - exR) <= tolerance) and (abs(g - exG) <= tolerance) and (abs(b - exB) <= tolerance):
            pimpg[x,y] = (0,0,255)
im.show()