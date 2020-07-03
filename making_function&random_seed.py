import re
import datetime
import random
from urllib.request import urlopen
from bs4 import BeautifulSoup


# random.seed(datetime.datetime.now('utc'))

def getLink(articleUrl):
    html = urlopen('https://en.wikipedia.org'+ articleUrl)
    bs_object = BeautifulSoup(html, 'html.parser')
    try:
        return bs_object.find("div", {"id":"bodyContent"}).findAll("a",href=re.compile("^(/wiki/)((?!:).)*$"))
    except:
        pass
    

links = getLink("/wiki/Kevin_Bacon")
print(links)
# returns a list of all the link on this page 

while len(links) > 0:
    new_article = links[random.randint(0, len(links)-1 )].attrs["href"]
    print(new_article)
    links = getLink(new_article)

    



