import requests
from bs4 import BeautifulSoup
url="https://www.codewithharry.com"
response=requests.get(url)
htmlcontent=response.content
# print(htmlc0ntent)
soup=BeautifulSoup(htmlcontent,"html.parser")
navbarsupportcontent=soup.find(id='navbarSupportedContent')
# print(navbarsupportcontent.contents)
# for ele in navbarsupportcontent.children:
#     print(ele)
for elem in navbarsupportcontent.stripped_strings:
    print(elem)

print("--------------------------------")
for item in navbarsupportcontent.parents:
    print(item.name)
print("--------------------------------")
for ite in navbarsupportcontent.children:
    print(ite.name)
print("--------------------------------")
print(navbarsupportcontent.previousSibling)
print("--------------------------------")
print(navbarsupportcontent.previousSibling.previousSibling)

print("--------------------------------")
elem=soup.select("#loginModal")
print(elem)

print("--------------------------------")
elemm=soup.select(".modal-footer")
print(elemm)