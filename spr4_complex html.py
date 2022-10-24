from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup


html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")

def name_list_story():
    bsObj = BeautifulSoup(html)
    nameList = bsObj.findAll("span", {"class":"green"})
    for name in nameList:
        return name.get_text()


# -----------------------------
# findAll(tag, attributes, recursive, text, limit, keywords)
bsObj = BeautifulSoup(html)
nameList = bsObj.findAll("span", {"class":"green","class":"red"})
#print(nameList)


# nameLis = bsObj.findAll(id="text")

# print(nameLis[0].get_text())


# bsObj = BeautifulSoup(html)
# nameList1 = bsObj.findAll(text="the prince")
# print(nameList1)

# x=bsObj.findAll(class_="green")
# for y in x:
#     print(y.get_text())

x=bsObj.NavigableString()
print(x)


