from urllib.request  import urlopen
from bs4 import BeautifulSoup


html = urlopen("http://pythonscraping.com/pages/page1.html")
bsobject = BeautifulSoup(html.read());

print(bsobject.nonExistentTag.someTag) # will return an exception AttributeError 
