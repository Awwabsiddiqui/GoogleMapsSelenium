import time
from selenium.webdriver.chrome.options import Options
from selenium import webdriver


def URL2Coordinates(url):
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome("chromedriver.exe", options=options)
    driver.get(url)
    time.sleep(5)
    url = driver.current_url

    lst = [i for i, ltr in enumerate(url) if ltr == '/']
    y = url[lst[5] + 2:]
    return [y[:y.find('/') - 4].split(',')[0], y[:y.find('/') - 4].split(',')[1]]


# url = 'https://www.google.com/maps/place/Buddha+Beauty+Point/@28.440274,77.0734384,14z/data=!4m7!3m6!1s0x390d2372d7bf9089:0xfcdd3a2faff9c178!8m2!3d28.4281585!4d77.0989666!15sCidzYWxvbnMgaW4gUmFpbCBWaWhhciwgR3VydWdyYW0sIEhhcnlhbmGSAQxiZWF1dHlfc2Fsb27gAQA!16s%2Fg%2F11nxrk1f_l?shorturl=1'
# url = 'https://www.google.com/maps/place/Elegante+Luxury+Salon/@28.4280497,77.098671,17z/data=!3m1!4b1!4m5!3m4!1s0x390d2341f3d74b51:0x113201a6024eaa1e!8m2!3d28.4280497!4d77.098671'
# url = "https://www.google.com/maps/place/DALIA'Z+UNISEX+HAIR+%26+BEAUTY+SALON/@28.4542434,77.0851923,17z/data=!3m1!4b1!4m5!3m4!1s0x390d196bc891a097:0x55ca7cd092d7896!8m2!3d28.4542434!4d77.0851923"
# url='https://www.google.com/maps/place/Lakme+Salon/data=!4m7!3m6!1s0x390d22009bc40001:0xa417aaa1f4540c74!8m2!3d28.4258797!4d77.09762!16s%2Fg%2F11d_9fb3hg!19sChIJAQDEmwAiDTkRdAxU9KGqF6Q?authuser=0&hl=en&rclk=1'
# print(URL2Longitude(url))
