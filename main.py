from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from CheckXLSX import CheckXLSX
from append2XLS import dict2List
from getMetaData import getMetaData
from dict2Mongo import dict2Mongo
from scroll import scroll


# key = 'salons in Rail Vihar, Gurugram, Haryana'
def mainMethod(key, x, y):
    url = "https://www.google.com/maps/search/" + str(str(key).replace(' ', '+'))

    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome("chromedriver.exe", options=options)
    driver.get(url)

    def getter(x, y):
        for i in range(x, y, 2):
            try:
                content = driver.find_element(By.XPATH,
                                              '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]/div[' + str(
                                                  i) + "]/div/a")
                # print(content.get_attribute('href'))
                if CheckXLSX(content.get_attribute('href')) == False:
                    dictionary = getMetaData(content.get_attribute('href'))
                    dictionary["SearchKeywords"] = key
                    dictionary["MapURL"] = content.get_attribute('href')
                    dict2List(dictionary)
                    dict2Mongo(dictionary)
            except:
                scroll(driver, content)
                getter(i, y)

    getter(x, y)

# mainMethod("salons in Rail Vihar, Gurugram, Haryana" , 3 , 10)
