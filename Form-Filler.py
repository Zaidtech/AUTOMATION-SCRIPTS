#!/usr/bin/env python3
"""
This script has been tested on various custom google forms and other various forms with  
few alteratios ..
Google forms which does not include the input type "token"  attribute are found 
to be safer than those who don't.
Any form contains various fields.

1. input text fields
2. radio
3. checkboxes
4. textareas
5. Uploads --- important . still working.
"""

import re
import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup

params = {} 
url = input("Enter the website url")
page = urlopen(url)

bs_obj = BeautifulSoup(page, 'html.parser')
# bs_obj.prettify() --> it's effects on the tags buried deep in the divs
requests.session()

input_tags = bs_obj.find_all('input')
# print(input_tags)
form_action = bs_obj.find('form')  # some pages have multiple form tags ...
text_tags = bs_obj.find_all('textarea')

for text in text_tags:
    try:
        print(text['name'])
        text['name'] = "Running around and fill this form"
    except:
        print('Key Error')

# if form_action.attrs['action'] == "" or None:
#     print("Form action not specifies")
# else:
# print(form_action)    
url = form_action.attrs['action']
print(f"Post request is send in here: {url}") 

# there might be some custom fields which are to be looked and inspected manually as they skip the scrapper
#  like params['entry.377191685'] = 'Faculty' 
# params['tos'] = 'true' 
# vary accordingly as at least an attck is just not that easy. ;-)


for tag in input_tags:
    try:
        print(tag.attrs['aria-label'])
    except:
        pass
    try:
        if tag.attrs['value'] == "" or None:
            tag.attrs['value'] = input(f"Enter the value of {tag.attrs['name']}")
            params[tag.attrs['name']] = tag.attrs['value']
            #  except:
            #      value= input(f"Enter the value of {tag.attrs['name']}")
            #      params[tag.attrs['name']] =  value
        else:
             params[tag.attrs['name']] = tag.attrs['value'].strip('\n')
    except:
        pass
print(params)
#  getting the dicts as printed here... which is to be submitted

while True: 
    requests.session()
    r  = requests.post(url, data=params)
    print(r.status_code) 
    
#  200 OK  ---> submitted 
#  400 BAD REQUEST ERROR --> input data corrupt or server incompatible  
#  401  UNAOUTHORIZED ACCESS --> validation failed  (need to deal with tokens and the cookies)





   
