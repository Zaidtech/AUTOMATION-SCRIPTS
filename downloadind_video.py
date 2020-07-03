from bs4 import BeautifulSoup
import urllib
import random
import urllib
import os
from urllib.request import urlopen, urlretrieve

def download(url):
    response =urlopen(url)
    doc  = response.read()
    soup = BeautifulSoup(doc, features="lxml")
    for link in soup.find_all('link'):
        url = (link.get('href'))
        # Extract filename from link URL
        filename = os.path.basename(url)
        file_data = os.path.splitext(filename)
        if len(file_data) > 1:
           file_ext = file_data[1]
           # this will allow you to download links with *.mp4 extension only
           if file_ext == ".mp4":
                print('Downloading....')
                urlretrieve(url, filename)

download('someurl')