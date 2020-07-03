from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

pages = set()
def get_links(page_url):
    global pages
    html = urlopen('http://en.wikipedia.org'+page_url)
    #  an base url to start searching from here here i am taking the wikipedia as a base
    bs_objectpage = BeautifulSoup(html, 'html.parser')
    for link in bs_objectpage.findAll("a", href=re.compile("^(/wiki/)")):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                print("Found a new page")
                new_page_link = link.attrs['href']
                print(new_page_link)
                pages.add(new_page_link)
                get_links(new_page_link)

get_links("")


