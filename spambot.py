import pyautogui
import time
import keyboard

time.sleep(3) # 3 saniye ye kadar yazmak istediğin yere tıkla
f=open("test.txt","r")

while keyboard.is_pressed('q') == False :
        for word in f:
            pyautogui.typewrite(word)
            pyautogui.press("enter")
