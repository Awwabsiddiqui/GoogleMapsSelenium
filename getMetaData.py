import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from URL2BusinessName import URL2BusinessName


def getMetaData(url):
    # driver = webdriver.Chrome('chromedriver.exe')
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome("chromedriver.exe", options=options)
    driver.get(url)
    initurl = driver.current_url
    oplist = driver.find_elements(By.CLASS_NAME, "CsEnBe")
    # print(len(oplist))
    dictionary = {'BusinessName': URL2BusinessName(url),
                  'TagLine': driver.find_element(By.CLASS_NAME, 'DkEaL.u6ijk').text}
    for obj in oplist:
        data = obj.get_attribute('aria-label')
        if data is not None and (':' in data):
            # print(data)
            if data.split(':')[0] == 'Plus code':
                dictionary["City"] = data.split(':')[1].strip()[data.split(':')[1].strip().find(' ') + 1:]
            dictionary[data.split(':')[0]] = data.split(':')[1].strip()
            if data.split(':')[0] == 'Website':
                dictionary["URL"] = obj.get_attribute('href')

    curURL = driver.current_url
    while curURL == initurl:
        curURL = driver.current_url
        time.sleep(0.5)

    lst = [i for i, ltr in enumerate(curURL) if ltr == '/']
    y = curURL[lst[5] + 2:]
    ls = [y[:y.find('/') - 4].split(',')[0], y[:y.find('/') - 4].split(',')[1]]
    dictionary['Longitude'] = ls[0]
    dictionary['Latitude'] = ls[1]
    # print(dictionary)
    return dictionary


# url = 'https://www.google.com/maps/place/Glowing+BeautySalon/@28.4308306,77.1015346,17z/data=!3m1!4b1!4m5!3m4!1s0x390d19db1da266c3:0xcfdd78b9156a9777!8m2!3d28.4308306!4d77.1015346'
# url='https://www.google.com/maps/place/Explorer+unisex+salon/@28.4510645,77.0816051,17z/data=!3m1!4b1!4m5!3m4!1s0x390d198cbac3f949:0xd89cb5e5dd2646e9!8m2!3d28.4510645!4d77.0816051'
# url = 'https://www.google.com/maps/place/Buddha+Beauty+Point/@28.440274,77.0734384,14z/data=!4m7!3m6!1s0x390d2372d7bf9089:0xfcdd3a2faff9c178!8m2!3d28.4281585!4d77.0989666!15sCidzYWxvbnMgaW4gUmFpbCBWaWhhciwgR3VydWdyYW0sIEhhcnlhbmGSAQxiZWF1dHlfc2Fsb27gAQA!16s%2Fg%2F11nxrk1f_l?shorturl=1'
url = 'https://www.google.com/maps/place/Lakme+Salon/data=!4m7!3m6!1s0x390d22009bc40001:0xa417aaa1f4540c74!8m2!3d28.4258797!4d77.09762!16s%2Fg%2F11d_9fb3hg!19sChIJAQDEmwAiDTkRdAxU9KGqF6Q?authuser=0&hl=en&rclk=1'
getMetaData(url)
