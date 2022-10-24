import requests
from bs4 import BeautifulSoup
url="https://www.codewithharry.com"
response=requests.get(url)
htmlcontent=response.content
# print(htmlc0ntent)
soup=BeautifulSoup(htmlcontent,"html.parser")
# print(soup.prettify)
title=soup.title.get_text()
print(title)
para=soup.findAll("p")
print(para)
# anchor=soup.findAll("a")
# print(anchor)
print("------------------\n")
cla=(soup.find("p")['class'])
print(cla)

print("------------------\n")
clas=(soup.find("p",class_="lead").get_text())
print(clas)

print("------------------\n")
anchor=soup.findAll("a")
all_link=set()
for link in anchor:
    if (link !='#'):
        all_link.add("https://www.codewithharry.com"+link.get('href'))
for linn in all_link:
    print(linn)

