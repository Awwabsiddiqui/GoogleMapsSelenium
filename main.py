from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from append2XLS import dict2List
from getMetaData import getMetaData
from scroll import scroll

options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome("chromedriver.exe", options=options)

key = 'salons in Rail Vihar, Gurugram, Haryana'
url = "https://www.google.com/maps/search/" + str(key.replace(' ', '+'))

driver.get(url)


def getter(x, y):
    for i in range(x, y, 2):
        try:
            content = driver.find_element(By.XPATH,
                                          '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]/div[' + str(
                                              i) + "]/div/a")
            print(content.get_attribute('href'))
            dictionary = getMetaData(content.get_attribute('href'))
            dictionary["SearchKeywords"] = key
            dictionary["MapURL"] = content.get_attribute('href')
            dict2List(dictionary)
        except:
            scroll(driver, content)
            getter(i, y)


getter(3, 200)
