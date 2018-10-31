#!usr/bin/python3
'''
    date:2018/10/29
    auth:YSilhouette
    version:0.1.0
'''

import requests
import xlwt
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

class One(object):
    sheet =None
    work_book = None
    row = 1

    def __init__(self):
        self.root_url ='http://wufazhuce.com'


    def get_headers(self):
        # ua = UserAgent()
        headers ={
            'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
            'Cookie':'_ga=GA1.2.1541802221.1540483266; ANGSESSID=r44k1em8j5jvgeuan2m6o12s54; _gid=GA1.2.188464988.1540807144',
        }
        return  headers

    def get_urls(self):
        for i in range(2000,2246):
            urls = self.root_url + '/one/'+str(i)
            self.get_data(urls)

    def get_data(self,url):
        try:
            response = requests.get(url,self.get_headers())
            if response.status_code == 200:
                # print(response.text)
                self.page_urls(response.text)
            else:
                print('请求页面异常',response.status_code)
                return None
        except Exception as e:
            print('请求页面异常',e)
            return None

    def page_urls(self,html):
        if html:
            bs = BeautifulSoup(html,'lxml')
            img_urls =bs.select('#main-container .one-imagen img')
            titles = bs.select('.one-titulo')
            img_authors =bs.select('.one-imagen-leyenda')
            contents = bs.select('.one-cita-wrapper .one-cita')
            times = bs.select('.one-cita-wrapper .one-pubdate')

            for title in titles:
                title1= title.text.strip()
            print(title1)

            for img_url in img_urls:
                url = img_url.get('src')
            print(url)

            for img_author in img_authors:
                img_auth = img_author.text.strip()
            print(img_auth)

            for content in contents:
                text_content = content.text.strip()
            print(text_content)

            for time in times:
                text_time = time.text.strip()
            print(text_time)

            self.sheet.write(self.row,0,title1)
            self.sheet.write(self.row,1,url)
            self.sheet.write(self.row,2,img_auth)
            self.sheet.write(self.row,3,text_time)
            self.sheet.write(self.row,4,text_content)
            self.row = self.row + 1


    def open_file(self):
        self.work_book = xlwt.Workbook(encoding='utf-8')
        self.sheet = self.work_book.add_sheet('One')
        self.sheet.write(0,0,'编号')
        self.sheet.write(0,1,'图片地址')
        self.sheet.write(0,2,'图片作者')
        self.sheet.write(0,3,'日期')
        self.sheet.write(0,4,'文字')

    def close_file(self):
        self.work_book.save('One.xls')



if __name__ == '__main__':
    one = One()
    one.open_file()
    one.get_urls()
    one.close_file()


