from urllib.request import urlretrieve , urlopen
from bs4 import BeautifulSoup

url = "https://web.whatsapp.com/"
html = urlopen(url)
bs_page_object = BeautifulSoup(html, 'html.parser')
image_locator = bs_page_object.find_all("img",{"class":"_2goTk _1Jdop _3Whw5"})
print(image_locator)
for img in image_locator:
    while i > 0:
        urlretrieve (img, f"image{i}.jpg")
        i +=1
        
