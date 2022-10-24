from urllib.request import urlopen
from bs4 import BeautifulSoup
# double = lambda x: x * 2
# print(double(5))

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
soup = BeautifulSoup(html)
element=soup.findall(lambda img: len(img.attrs) == 1)
