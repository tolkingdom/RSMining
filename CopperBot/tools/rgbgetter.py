from pynput.mouse import Listener
import pyautogui
import cv2
import logging
import os

dirname1 = os.path.dirname(os.path.abspath(__file__))
print(dirname1)
os.chdir(dirname1)

logging.basicConfig(filename="mouse_log.txt", level=logging.DEBUG, format='%(asctime)s: %(message)s')
rgblist = (113,73,41),(91,59,33),(82,53,29),(79,50,27),(129,83,46),(101, 65, 35),(95, 61, 34),(75, 48, 26),(69, 44, 25),(72, 47, 25)
ironlist = [(0,0,0)]

def on_click(x, y, button, pressed):
    if pressed:
        x,y = list(pyautogui.position())
        z = pyautogui.pixel(x,y)
        if z in ironlist:
            pass
        else:
            print(z)
            ironlist.append(z)
    if len(ironlist) >= 11:
        logging.info(str(ironlist))

with Listener(on_click=on_click) as listener:
    listener.join()


