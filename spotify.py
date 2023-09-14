
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time



class Spotify:
    def __init__(self,username,password):
        self.browserProfile = webdriver.ChromeOptions()
        self.browserProfile.add_experimental_option('prefs', {'intl.accept_languages':'en,en_US'})
        self.browser = webdriver.Chrome('chromedriver.exe', chrome_options=self.browserProfile)
        self.username = username
        self.password = password

    def signIn(self):
        #self.browser.get("https://open.spotify.com/")
        self.browser.get("https://accounts.spotify.com/tr/login")
        time.sleep(2)
        #self.browser.find_element_by_xpath("//*[@id='main']/div/div[2]/div[1]/header/div[4]/button[2]").click()
        #time.sleep(2)
        
        #self.browser.find_element_by_xpath("//*[@id='login-button']").click()
        
        usernameInput = self.browser.find_element_by_xpath("//*[@id='login-username']")
        passwordInput = self.browser.find_element_by_xpath("//*[@id='login-password']")
        time.sleep(2)
        usernameInput.send_keys(self.username)
        time.sleep(2)
        passwordInput.send_keys(self.password)
        time.sleep(2)
        #self.browser.find_element_by_xpath("//*[@id='login-button']").click()
        time.sleep(2)

    def getPlay(self):
        self.browser.get("https://open.spotify.com/playlist/37i9dQZF1DXbITWG1ZJKYt")
        time.sleep(2)
        self.browser.find_element_by_xpath("//*[@id='main']/div/div[2]/div[4]/div[1]/div/div[2]/div/div/div[2]/section/div[3]/div/button[1]").click()
        time.sleep(2)
        self.browser.find_element_by_xpath("//*[@id='main']/div/div[2]/div[3]/footer/div/div[2]/div/div[1]/div[1]/button").click()
        
        self.browser.find_element_by_xpath("//*[@id='main']/div/div[2]/div[3]/footer/div/div[2]/div/div[1]/div[4]/button").click()
        time.sleep(2)
        
        
spoti = Spotify(username, password)
spoti.signIn()
time.sleep(2)
spoti.getPlay()
 