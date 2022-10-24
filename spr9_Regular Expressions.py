from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
# html = urlopen("http://www.pythonscraping.com/pages/page3.html")
# bsObj = BeautifulSoup(html)
# images = bsObj.findAll("img", {"src":re.compile("\.\.\/img\/gifts/img.*\.jpg")})
# for image in images:
#     print(image["src"])
# ----------------------


# NameAge='''Janice is 22 and Theon is 33
# Gabriel is 44 and Joye is 21
# '''
# ages=re.findall(r'\d{1,3}',NameAge)
# names=re.findall(r'[A-Z][a-z]*',NameAge)
# agedict={}
#
# x=0
#
# for name in names:
#     agedict[name]=ages[x]
#     x+=1
# print(agedict)

# ----------------------

data="we need to inform him with the latest information"

# if re.search("inform",data):
#     print("There is inform")
# allinfo=re.findall('inform',data)
# print(allinfo)

# ----------------------

#
# finditr=re.finditer("inform",data)
# for i in finditr:
#     location=i.span()
#     print(location)
#     print(i)
#
# # ----------------------
# splitword=[]
# for i in data.split():
#     splitword.append(i)
#
# print(splitword)
# for word in splitword:
#     if re.search("[w]",word):
#         print(word)


# words='hot,mat,rat,that'
# regex=re.compile('[r]at')
# words=regex.sub("replaced",words)
# print(words)


# random_str="keep the blue flag flaying high"
# regex=re.compile('blue')
# randmstr=regex.sub("red and green",random_str)
# print(randmstr)

# rens="477816sd70"
# print("matches:",len(re.findall("\d",rens)))
# print("matches:",len(re.findall("\D",rens)))
# print("matches:",len(re.findall("\d{7}",rens)))



# identifying the phone numbers
# \W it means anything

# phn="""412-158-55551"""
# if re.search("\w{3}-\w{3}-\w{4}",phn):
#     print("it is a phone number")
# email="shihab18015@ggmail.com"
# print("Email Matches:",)
