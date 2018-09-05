# encoding:utf-8
import requests
from bs4 import BeautifulSoup
from lxml import etree
import urllib.request
import ssl
import os
ssl._create_default_https_context =ssl._create_unverified_context


# 指定下载路径下载图片
def downloadImg(url):
    imgurl=url
    imgName =imgurl.split('/')[-1]
    imgPath =os.path.join('/Users/gaozhiyong/Desktop/imgs',imgName)
    print("下载" + imgName + '中')
    urllib.request.urlretrieve(imgurl,filename=imgPath)
    print( imgName + '下载已完成')

# 网页解析器
def get_Page(pageUrl):
    headers={
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
    }
    req = requests.get(pageUrl,headers=headers)
    req.encoding='utf-8'
    soup =BeautifulSoup(req.content,'lxml')
    img_list =soup.find_all('img',attrs={'class':'lazy image_dtb img-responsive'})
    for img in img_list:
        url =img['data-original']
        downloadImg(url)

def main():
    PAGE_BASE_URL = "https://www.doutula.com/article/list/?page="
    PAGE_URL_LIST = []
    # range, 左闭区间，右边开区间
    # URL下载器，存储进入列表内
    for i in range(1, 5):
        page_url = PAGE_BASE_URL + str(i)
        PAGE_URL_LIST.append(page_url)
    print(PAGE_URL_LIST)

    for pageUrl in PAGE_URL_LIST:
        print(pageUrl)
        get_Page(pageUrl)


if __name__ == '__main__':
    main()



