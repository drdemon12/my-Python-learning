from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

#pyautogui.displayMousePosition()  #buradan mouse ın konumunu bulup aşağı yazıyoruz.

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01) #This pauses the script for 0.01 seconds
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q') == False:
    
    if pyautogui.pixel(581, 400)[0] == 0: # x,y ve rgb r=0,g=1,b=2 
        click(581, 400)
    if pyautogui.pixel(682, 400)[0] == 0:
        click(682, 400)
    if pyautogui.pixel(770, 400)[0] == 0:
        click(770, 400)
    if pyautogui.pixel(869, 400)[0] == 0:
        click(869, 400)