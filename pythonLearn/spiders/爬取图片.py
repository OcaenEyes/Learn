import requests
from bs4 import BeautifulSoup
import urllib
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

# targetPath ="D:\pythonSpiders\mImges"
baseUrl = "http://www.27270.com/ent/meinvtupian/"

res = requests.get(baseUrl)
# 设置编码格式
res.encoding = "urf8"
# 读取到soup里
soup = BeautifulSoup(res.text, "html.parser")
# 筛选有多少个jpg标签,并且打印出来
soupImgList = soup.find_all('img')
lenth = len(soupImgList)
for i in range(lenth):
    imgList = soupImgList[i].attrs['src']
    print(imgList)
picUrl = imgList[0:lenth - 2]
print(picUrl)
b = str(i)
fileName = b + '.' + 'jpg'
print(fileName)
u = urllib.request.urlopen(picUrl)
data = u.read()
f = open(fileName, 'wb')
f.write(data)
print(u"正在悄悄保存她的一张图片为", fileName)
f.close()
