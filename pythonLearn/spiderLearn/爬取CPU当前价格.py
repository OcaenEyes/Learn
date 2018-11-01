#!usr/bin/python3

'''
    auth:YSilhouette
    date:2018/10/31
    version:0.1.0
'''

import requests
import xlwt
from bs4 import BeautifulSoup

class CPUPrice(object):
    sheet = None
    workbook =None
    row = 1



    def __init__(self):
        self.BASE_URL ='http://detail.zol.com.cn/cpu'

    def get_urls(self):
        for key in ['1177026','1233483','1233484']:
            urls = self.BASE_URL + '/index' + key  + '.shtml'
            self.get_pages(urls)
            print(urls)

    def get_headers(self):
        headers ={
            'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36'
        }
        return headers

    def get_price(self,html):
        soup = BeautifulSoup(html,'html.parser')
        prices = soup.select('.price-type')
        print('参考价格',prices)
        jdprices = soup.select('.b2c-jd .price')
        print('京东价格',jdprices)
        tmallprices = soup.select('.b2c-tmall .price')
        print('天猫价格',tmallprices)

    def get_pages(self,url):
        try:
            response = requests.get(url,self.get_headers())
            if response.status_code == 200:
                self.get_price(response.text)
            else:
                print('请求页面异常',response.status_code)
        except Exception as e:
            print('请求页面异常',e)
            return None





if __name__ =='__main__':
    cpuPrice = CPUPrice()
    cpuPrice.get_urls()





