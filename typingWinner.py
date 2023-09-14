
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class typing:
    def __init__(self,username,password=("demon12")):
        self.browserProfile = webdriver.ChromeOptions()
        self.browserProfile.add_experimental_option('prefs', {'intl.accept_languages':'en,en_US'})
        self.browser = webdriver.Chrome('chromedriver.exe', chrome_options=self.browserProfile)

        self.username = username
        self.password = password
        self.username1 = username1
        self.username2 = username2

    def signIn(self):
        self.browser.get("https://www.speedtypingonline.com/login")

        usernameInput = self.browser.find_element_by_xpath("//*[@id='username']")
        usernameInput.send_keys(self.username)

        passwordInput = self.browser.find_element_by_xpath("//*[@id='password']")
        passwordInput.send_keys(self.password)
        self.browser.find_element_by_xpath("//*[@id='pageMain']/div/div[3]/form/input[2]").click()

        
    def sayi(self,username1):

        self.browser.get("https://www.speedtypingonline.com/games/type-the-alphabet.php")
        self.browser.find_element_by_xpath("//*[@id='blockDivContainer']").click()
        
        username1Input = self.browser.find_element_by_xpath("//*[@id='blockDivContainer']")
        username1Input.send_keys(self.username1)
        time.sleep(0.01)
        username1Input.send_keys(self.username2)

typee = typing(username,password)
typee.signIn()
typee.sayi(username1)
