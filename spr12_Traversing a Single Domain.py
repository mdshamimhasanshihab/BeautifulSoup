# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# html = urlopen("https://www.facebook.com/shamim.hasanshihab.3")
# bsObj = BeautifulSoup(html)
# for link in bsObj.findAll("a"):
#     if 'href' in link.attrs:
#         if link.attrs['href'][0]=='h':
#             print(link.attrs['href'])


from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
html = urlopen("http://en.wikipedia.org/wiki/Kevin_Bacon")
bsObj = BeautifulSoup(html)
for link in bsObj.find("div", {"id":"bodyContent"}).findAll("a",
    href=re.compile("^(/wiki/)((?!:).)*$")):
    if 'href' in link.attrs:
        print(link.attrs['href'])