import json
from datetime import datetime
from getNetclanID import getNetClanId
from JSON2Mongo import JSON2Mongo

def dict2Mongo(dict):
    with open('merchant.json') as f:
        jsn = json.load(f)

        if dict.get('Phone') is not None:
            jsn.update({'phone' : int(dict.get('Phone').replace(' ' , ''))})
            jsn.update({'fullPhone' : str(jsn['countryCode'])+str(int(dict.get('Phone').replace(' ' , '')))})

        jsn['bio'].update({'data' : dict.get('TagLine' , "")})
        jsn['category'].update({'data': dict.get('Category', "")})

        jsn['companyName'].update({'data' : dict.get('BusinessName' , "")})
        jsn.update({'merchantName': dict.get('BusinessName', "")})

        jsn.update({'profilePicUrl' : dict.get('bucketURL' , "")})

        jsn['location']['coordinates'][1] = float(dict.get('Longitude' , 0.0))
        jsn['location']['coordinates'][0] = float(dict.get('Latitude' , 0.0))

        jsn['website'].update({'data' : dict.get('URL' , "")})

        jsn['places']['data'][0]['name'] = str(dict.get('City' , ",")).split(',')[0].strip()
        jsn['places']['data'][0]['state'] = str(dict.get('City' , ",")).split(',')[1].strip()

        jsn.update({'netClanId': getNetClanId(str(dict.get('BusinessName', "")) , str(dict.get('City' , ",")).split(',')[0].strip())})

        d = datetime.strptime("2017-10-13T10:53:53.000Z", "%Y-%m-%dT%H:%M:%S.000Z")
        jsn['createdDate'] = d
        jsn['modifiedDate'] = d


        # print(json.dumps(jsn))
        print(jsn)
        JSON2Mongo(jsn)


# dict={"Phone" : "2" , "BusinessName":"someBusiness" , "URL" : "someURL"}
# dict2Mongo(dict)

