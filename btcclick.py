from asyncore import loop
from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

#pyautogui.displayMousePosition()
#requirements = pyautogui, pillow


def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01) #This pauses the script for 0.01 seconds
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

pyautogui.click(591, 1043)

while keyboard.is_pressed('q') == False:
    if pyautogui.click(942, 883) == 0: # x,y ve rgb r=0,g=1,b=2 
        pyautogui.click(button='left', clicks=1000, interval=0.001) 
    
   