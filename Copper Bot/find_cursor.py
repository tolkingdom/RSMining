import time

import pyautogui


def calibrate():
    l,t,w,h = pyautogui.locateOnScreen("img/runelite.png")
    print (l,t,w,h)
    return l,t+27



def convertxy(x,y):
    x2=x-x0
    y2=y-y0
    print(x2,y2)
    return x2,y2


x0,y0 = calibrate()
bottomright = x0+765,y0+502


if __name__ == '__main__':
    print('Press Ctrl-C to quit.')
    x0,y0 = calibrate()
    
    def calibrate():
        l,t,w,h = pyautogui.locateOnScreen("img/runelite.png")
        print (l,t,w,h)
        return l,t+27



    def convertxy(x,y):
        x2=x-x0
        y2=y-y0
        print(x2,y2)
        return x2,y2


    
    try:
        while True:
            # Get and print the mouse coordinates.
            x, y = pyautogui.position()
            x2,y2 = convertxy(x,y)
            positionStr = 'X: ' + str(x).rjust(4) + ' X2: ' + str(x2).rjust(4) + ' Y: ' + str(y).rjust(4) + ' Y2: ' + str(y2).rjust(4)
            print("\r", positionStr, end="", flush=True)
            time.sleep(0.25)
    except KeyboardInterrupt:
        print('\nDone.')
