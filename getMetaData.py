import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from URL2BusinessName import URL2BusinessName
from downloadImage import downloadImage


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
            if data.split(':')[0] == 'Website':
                dictionary["URL"] = obj.get_attribute('href')
            dictionary[data.split(':')[0]] = data.split(':')[1].strip()

    curURL = driver.current_url
    while curURL == initurl:
        curURL = driver.current_url
        time.sleep(0.5)

    lst = [i for i, ltr in enumerate(curURL) if ltr == '/']
    y = curURL[lst[5] + 2:]
    ls = [y[:y.find('/') - 4].split(',')[0], y[:y.find('/') - 4].split(',')[1]]
    dictionary['Longitude'] = ls[0]
    dictionary['Latitude'] = ls[1]

    if "Phone" in dictionary:

        # mainImg = driver.find_element(By.XPATH , '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[1]/div[1]/button/img').get_attribute('src')
        # print(mainImg)
        # downloadImage(str(mainImg) , dictionary.get('Phone'), 1)

        imgList = driver.find_elements(By.CLASS_NAME, "DaSXdd")
        # print(len(imgList))
        i = 1
        for img in imgList:
            src = img.get_attribute('src')
            downloadImage(str(src), dictionary.get('Phone'), i)
            i += 1

    # print(dictionary)
    driver.quit()
    return dictionary

# url = 'https://www.google.com/maps/place/Lakme+Salon/data=!4m7!3m6!1s0x390d22009bc40001:0xa417aaa1f4540c74!8m2!3d28.4258797!4d77.09762!16s%2Fg%2F11d_9fb3hg!19sChIJAQDEmwAiDTkRdAxU9KGqF6Q?authuser=0&hl=en&rclk=1'
# url = 'https://www.google.com/maps/place/Glowing+BeautySalon/data=!4m7!3m6!1s0x390d19db1da266c3:0xcfdd78b9156a9777!8m2!3d28.4308306!4d77.1015346!16s%2Fg%2F11gzpnff0x!19sChIJw2aiHdsZDTkRd5dqFbl43c8?authuser=0&hl=en&rclk=1'
# url='https://www.google.com/maps/place/Hello+Gorgeous+Unisex+Salon+%26+Makeup+Studio/data=!4m7!3m6!1s0x390d18aa77c5acad:0xa463c39682228146!8m2!3d28.4287532!4d77.0988616!16s%2Fg%2F11byyqb1r6!19sChIJrazFd6oYDTkRRoEigpbDY6Q?authuser=0&hl=en&rclk=1'
# url='https://www.google.com/maps/place/Buddha+Beauty+Point/data=!4m7!3m6!1s0x390d2372d7bf9089:0xfcdd3a2faff9c178!8m2!3d28.4281585!4d77.0989666!16s%2Fg%2F11nxrk1f_l!19sChIJiZC_13IjDTkReMH5ry863fw?authuser=0&hl=en&rclk=1'
# url='https://www.google.com/maps/place/Explorer+unisex+salon/data=!3m1!4b1!4m5!3m4!1s0x390d198cbac3f949:0xd89cb5e5dd2646e9!8m2!3d28.4510645!4d77.0816051'

# print(getMetaData(url))
