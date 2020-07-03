import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen

# Trying out the form with the tokens not yet able to do it ..

params = {

'entry.1293209251':"купить емейл адрес chekin", 
'entry.1675561640': "HackereRussia",
'entry.415491173': "Univesty Sinki",
'entry.799109460': "https://www.linkedin.com/ru/купить емейл адрес//s3hjmb3jjk",
'entry.896106191': "No",
'emailAddress': "купить2332адрес@gmail.com",
'entry.896106191_sentinel': None ,
'entry.1670422598_sentinel': None , 
'fvv': '1',
'draftResponse': '[null,null,"-4742652278693643138"]',
'pageHistory': '0',
'token': 'E9FM63IBAAA.rEfWhhWQTj1dGjKsssr1SA.l5lUlPHlblVRZ9R4ot41Yw',
'fbzx': '-4742652278693643138'

}

# # 'draftResponse':"%5B%5B%5Bnull%2C1293209251%2C%5B%22Mohd.+Zaid+Ali%22%5D%0D%0A%2C0%5D%0D%0A%2C%5Bnull%2C415491173%2C%5B%22Aligarh+Muslim+University+Z.H.C.E.T+%22%5D%0D%0A%2C0%5D%0D%0A%2C%5Bnull%2C1675561640%2C%5B%22Mohd.+Zaid%22%5D%0D%0A%2C0%5D%0D%0A%2C%5Bnull%2C799109460%2C%5B%22https%3A%2F%2Fwww.linkedin.com%2Fin%2Fzaid-ali-b91a78192%2F%22%5D%0D%0A%2C0%5D%0D%0A%2C%5Bnull%2C896106191%2C%5B%22No%22%5D%0D%0A%2C0%5D%0D%0A%5D%0D%0A%2Cnull%2C%22-4742652278693643138%22%2Cnull%2Cnull%2Cnull%2C%22mohd.zaid07ali%40gmail.com%22%2C1%5D%0D%0A",
# # 'pageHistory': '0',
# # 'token': 'E9FM63IBAAA.rEfWhhWQTj1dGjKsssr1SA.l5lUlPHlblVRZ9R4ot41Yw',
# # 'fbzx': '-4742652278693643138'
# # # 2979810754366461272
# }


# params = {} 

url = "https://docs.google.com/forms/d/e/1FAIpQLScbmKigNglbHoKia1alYDSw-ASt3dp0TB8CuWuMTJl5hjwoxA/viewform"

url_r = "https://docs.google.com/forms/d/e/1FAIpQLScbmKigNglbHoKia1alYDSw-ASt3dp0TB8CuWuMTJl5hjwoxA/formResponse"

# input_tags = bs_obj.find_all('input')

# print(input_tags.content)
page = urlopen(url)

requests.session()












while True: 
    requests.session()
    r  = requests.post(url_r, data=params)
    print(r.status_code) 

