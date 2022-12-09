import random
import string


def getNetClanId(name , city):
    try:
        name  = name.upper()
        city = city.upper()
        netClanID = ""
        nameArr = name.split(' ')
        if(len(nameArr[0]) >1):
            netClanID = netClanID + nameArr[0][0] + nameArr[0][0]
        else:
            netClanID = netClanID + name[0] + name[0]

        city = city + "ZZZZ"
        netClanID = netClanID + city[0:4]

        netClanID = netClanID + str(''.join(random.choices(string.ascii_uppercase +string.digits, k=7)))
    except Exception as e:
        print(e)

    return netClanID


# print(getNetClanId("awwab siddiqui" , "delh"))