import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def downloadImage(url , phone , i):

    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome("chromedriver.exe", options=options)
    driver.get(url)
    try:
        with open(str(phone)+'/Logo'+str(i)+'.png', 'wb') as file:
            l = driver.find_element(By.XPATH , '/html/body/img')
            file.write(l.screenshot_as_png)
    except:
        os.mkdir(str(phone))
        downloadImage(url, phone, i)

    driver.quit()


# downloadImage("https://lh5.googleusercontent.com/p/AF1QipO98kv10c3fx-PYeoQ1ntVABYu1Wy9_jDWFvQU=s644-k-no" , 9999 , 2)
#
# aoRNLd kn2E5e NMjTrf lvtCsd    (main)
# ofKBgf(button)   DaSXdd(img)
# m6QErb (internal imgs all clicker) --- ofKBgf to click
# U39Pmb