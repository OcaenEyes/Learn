#!/usr/bin/python
#_*_coding:utf-8_*_
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

import requests

url = 'http://www.baidu.com'
content = requests.get(url)
print(content.encoding,content.headers)
print(content.text)