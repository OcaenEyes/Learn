#!usr/bin/python3
'''
    date:2018/11/01
    auth:YSilhouette
    version:V0.1.0
'''

import requests
from bs4 import BeautifulSoup


class JuDou(object):

    sheet = None
    row =1


    def __init__(self):
        self.base_url = 'https://judouapp.com/api/v6/op/sentences/daily?app_key=af66b896-665e-415c-a119-6ca5233a6963&channel=App%20Store&device_id=b00d4922a80653c7123e8cac7268833b&device_type=iPhone9%2C1&page=1&per_page=45&platform=ios&signature=4895b0095efd0238e5f13b3de9a7a301&system_version=10.3&timestamp=1540934759&token=afe61ca35b003b04330a6cd92a51b56c&version=3.5.7&version_code=41'

    def get_url(self):
        try:
            response = requests.get(self.base_url,headers={'Content-Type':'application/json',})
            if response.status_code == 200:
                response.encoding='utf-8'
                self.data = response.text

            else:
                print('请求异常',response.status_code)
        except Exception as e:
            print('请求异常',e)
            return None

    def get_data(self):
        print(self.data)





if __name__ == '__main__':
    juDou =JuDou()
    juDou.get_url()
    juDou.get_data()



