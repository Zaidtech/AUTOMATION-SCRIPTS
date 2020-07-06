import re
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://en.wikipedia.org/wiki/Kevin_Bacon')
bs_object = BeautifulSoup(html, 'html.parser')


# for link in bs_object.find("a"):
#     if 'href' in link.attrs:
#         print(link.attrs['href'])
# Can modify the above code a bit to get only those links which corresponds to article 

for link in bs_object.find("div", {"id":"bodyContent"}).findAll("a",href=re.compile("^(/wiki/)((?!:).)*$")):
    if 'href' in link.attrs:
        print(link.attrs['href'])


