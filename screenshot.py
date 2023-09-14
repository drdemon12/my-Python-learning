import pyautogui
import time
import datetime
#im1 = pyautogui.screenshot(region=(660,350,600,400)) # burası değiştirilebilir.
#x,y , genişlik, yükseklik
#time.sleep(3) #3 saniye sonra ss alabilir

im1 = pyautogui.screenshot(region=(0,0,1920,1080))
x = datetime.datetime.now()
print(x.strftime("%Y-%m-%d__%H:%M:%S"))
#pyautogui.screenshot(r"screenshot1{x}.png",)
    


#im1.save(r"C:\Users\KAPLAN\Downloads\savedimage.png")
