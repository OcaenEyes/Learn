from urllib import request
import re
import ssl
from bs4 import BeautifulSoup

ssl._create_default_https_context = ssl._create_unverified_context

url = 'https://baike.baidu.com/item/QQ%E7%A9%BA%E9%97%B4/146945?fr=aladdin'
req = request.Request(url)
resp = request.urlopen(req)
html = resp.read().decode('utf-8')
print(html)
# soup = BeautifulSoup(html)
