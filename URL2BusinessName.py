def URL2BusinessName(url):
    return url[34:][:url[34:].find('/')].replace('+', ' ').replace('%26', '&')

# url = 'https://www.google.com/maps/place/Buddha+Beauty+Point/@28.440274,77.0734384,14z/data=!4m7!3m6!1s0x390d2372d7bf9089:0xfcdd3a2faff9c178!8m2!3d28.4281585!4d77.0989666!15sCidzYWxvbnMgaW4gUmFpbCBWaWhhciwgR3VydWdyYW0sIEhhcnlhbmGSAQxiZWF1dHlfc2Fsb27gAQA!16s%2Fg%2F11nxrk1f_l?shorturl=1'
# url='https://www.google.com/maps/place/Lakme+Salon/data=!4m7!3m6!1s0x390d22009bc40001:0xa417aaa1f4540c74!8m2!3d28.4258797!4d77.09762!16s%2Fg%2F11d_9fb3hg!19sChIJAQDEmwAiDTkRdAxU9KGqF6Q?authuser=0&hl=en&rclk=1'
# URL2BusinessName(url)
