from google.cloud import storage

def getURL(item_name):
    storage_client = storage.Client.from_service_account_json('netclan-1e352a4469b2.json')

    # file_list = storage_client.list_blobs('netclandev' , prefix='profile/multipart')
    # file_list = [file.name for file in file_list]
    # print(len(file_list))

    bucket = storage_client.bucket('netclandev')
    url = bucket.blob(item_name).generate_signed_url(100)
    print(url)


def Upload2Cloud(phone , i):
    storage_client = storage.Client.from_service_account_json('netclan-1e352a4469b2.json')

    bucket = storage_client.bucket('netclandev')

    blob = bucket.blob('profile/multipart/' + str(phone)+'_'+str(i)+'.png')
    blob.upload_from_filename('images/'+str(phone)+"/"+str(phone)+'_'+str(i)+ '.png')

    return ('https://storage.googleapis.com/netclandev/profile/multipart/' + str(phone) + '_' + str(i) + ".png").replace(' ','%20')


# getURL("requirementss.txt")
# Upload2Cloud('9718' , 1)
# https://storage.googleapis.com/netclandev/profile/multipart/075033%2097809_7.png
