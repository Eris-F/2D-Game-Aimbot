from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
#X:  521 Y:  370 RGB: (255, 191,  86)

time.sleep(5)

def click(x,y):
    win32api.SetCursor((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

while keyboard.is_pressed('q') == False:

    pic = pyautogui.screenshot(region=(580,250,800,600))
    width , height = pic.size


    for x in range(0,width,5):
        for y in range(0,height,5):

            r,g,b = pic.getpixel((x,y))

            if b == 195:
                click(x,y)
                time.sleep(1)
                break