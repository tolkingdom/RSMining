import cv2  
import numpy as np 
import os
import pyautogui

dirname1 = os.path.dirname(__file__)
os.chdir(dirname1)


def imgmatchscreen(small, region1=None, threshold=0.8):
    img = np.array(pyautogui.screenshot(region=region1))
    image = img[:, :, ::-1].copy()
    template = cv2.imread(small) 
    h,w,ch = template.shape
    result = cv2.matchTemplate(image,template,cv2.TM_CCOEFF_NORMED)  
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    #print(' Best match top left pixel found at %s' % str(max_loc))
    #print(' Best match confidence %s' % max_val)
    x,y = max_loc
    imgbox = x,y,w,h
    return imgbox




def imgmatchscreenall(small, region1=None, threshold=0.9):
    locbox = []
    img = np.array(pyautogui.screenshot(region=region1))
    image = img[:, :, ::-1].copy()
    template = cv2.imread(small) 
    h,w,ch = template.shape
    result = cv2.matchTemplate(image,template,cv2.TM_CCOEFF_NORMED) 
    locations = np.where(result >= threshold)
    locations = list(zip(*locations[::-1]))
    #print(len(locations))
    for i in locations:
        #print(i)
        x,y =  i
        locbox.append((x,y,w,h))
    return locbox



#print(imgmatchscreenall("img/ironitem.png",region1=(0,0,5800,900)))


needle = cv2.imread("img/minerocks.png")
haystack = cv2.imread("img/Large.png")
result = cv2.matchTemplate(haystack,needle,cv2.TM_CCOEFF_NORMED,)

cv2.imshow('z',result)
cv2.waitKey()
m,ma,ml,mal = cv2.minMaxLoc(result)
print(result)
print(ma,ml)







