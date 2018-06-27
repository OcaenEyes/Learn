#!/usr/bin/python
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

resp = urlopen('https://baike.baidu.com').read().decode('utf-8')

soup = BeautifulSoup(resp,'html.parser')

print(soup)
