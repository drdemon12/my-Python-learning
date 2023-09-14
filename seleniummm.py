from selenium import webdriver
import time

result = webdriver.Chrome()
url = "https://www.wikipedia.org/"
result.get(url)
time.sleep(1.4)

result.maximize_window()
time.sleep(1.6)

result.save_screenshot("screenshot_1.png")
print(result.title)
time.sleep(1.2)
result.close()
