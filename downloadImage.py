import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from Upload2Cloud import Upload2Cloud


def downloadImage(url, phone, i):
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome("chromedriver.exe", options=options)
    driver.get(url)
    try:
        with open("images/" + str(phone) + '/'+ str(phone) +"_"+ str(i) + '.png', 'wb') as file:
            writeImg = driver.find_element(By.XPATH, '/html/body/img')
            file.write(writeImg.screenshot_as_png)
    except:
        os.mkdir("images/" + str(phone))
        downloadImage(url, phone, i)

    driver.quit()
    return Upload2Cloud(phone , i)

# downloadImage("https://lh5.googleusercontent.com/p/AF1QipO98kv10c3fx-PYeoQ1ntVABYu1Wy9_jDWFvQU=s644-k-no" , 9999 , 2)
