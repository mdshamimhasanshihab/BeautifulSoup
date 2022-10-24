# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# html = urlopen("http://www.pythonscraping.com/exercises/exercise1.html")
# b = BeautifulSoup(html.read())
# print(b)
# # print(b.div)
# # print(b.head)
# # print(b.body.div)
#
# b'<html>\n<head>\n<title>A Useful Page</title>\n</head>\n<body>\n<h1>An Interesting Title</h1>\n<div>\nLorem ipsum dolor ' \
# b'sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim' \
# b' veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in ' \
# b'reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. ' \
# b'Excepteur sint occaecat cupidatat non proident, ' \
# b'sunt in culpa qui officia deserunt mollit anim id est laborum.\n</div>\n</body>\n</html>\n'

import requests
from bs4 import BeautifulSoup
response=requests.get("http://www.pythonscraping.com/exercises/exercise1.html")
print(response.status_code)
print(response.text)

