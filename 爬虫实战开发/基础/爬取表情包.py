import ssl
import sys
import os
import requests
from lxml import etree
import urllib.request
from bs4 import BeautifulSoup
# 设置https协议证书可允许
ssl._create_default_https_context = ssl._create_unverified_context

# 图片下载器


def download_img(img_url):
    imgName = img_url.split('/')[-1]
    imgPath = os.path.join('D:\pythonSpiders\mImges', imgName)
    urllib.request.urlretrieve(img_url, filename=imgPath)
    print(imgName + '下载已完成')

# 网页解析器


def get_page(page_url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0'}
    req = requests.get(page_url, headers=headers)
    req.encoding = 'utf-8'
    soup = BeautifulSoup(req.content, 'lxml')
    img_list = soup.find_all(
        'img', attrs={'class': 'lazy image_dtb img-responsive'})
    for img in img_list:
        img_url = img['data-original']
        download_img(img_url)

# 网页管理器


def main():
    PAGE_BASE_URl = "https://www.doutula.com/article/list/?page="  # 设置基本链接
    PAGE_URL_LIST = []  # 初始化页面URL列表
    for i in range(1, 100):
        pages_url = PAGE_BASE_URl + str(i)
        PAGE_URL_LIST.append(pages_url)  # 每个页面url加入列表中
    print(PAGE_URL_LIST)

    for page_url in PAGE_URL_LIST:
        print(page_url)
        get_page(page_url)

if __name__ == '__main__':
    main()
