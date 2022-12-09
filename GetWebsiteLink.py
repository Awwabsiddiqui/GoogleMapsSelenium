from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# url = "https://clutch.co/directory/mobile-application-developers"
url="https://clutch.co/developers/react-native"
options = Options()
# options.add_argument("--headless")
# options.add_argument('--proxy-server=http://myproxy:port')
driver = webdriver.Chrome("chromedriver.exe", options=options)
driver.get(url)

# waiter = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, "website-link__item")))

def gets(className , attribute):
    content = driver.find_elements(By.CLASS_NAME, className)
    # print(len(content))
    for cc in content:
        print(cc.get_attribute(attribute))



gets("website-link__item" , "href")

gets("provider-detail-contact" , "href")

gets("locality" , "innerHTML")

# content = driver.find_elements(By.CLASS_NAME,'website-link__item')
# # print(len(content))
# for cc in content:
#     print(cc.get_attribute('href'))
#
# content1 = driver.find_elements(By.CLASS_NAME, 'provider-detail-contact')
# # print(len(content1))
# for cc1 in content1:
#     print(cc1.get_attribute('href'))
#
# content3 = driver.find_elements(By.CLASS_NAME , 'locality')
# # print(len(content3))
# for cc3 in content3:
#     print(cc3.get_attribute('innerHTML'))

