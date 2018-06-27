#!/usr/bin/python
#_*_ coding:utf-8_*_

import sys
import io
from urllib import request
import ssl
from bs4 import BeautifulSoup

ssl._create_default_https_context = ssl._create_unverified_context

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')


req =request.Request('https://user.qzone.qq.com/1450136519')
req.add_header('method', 'GET')
req.add_header('referer', 'https://user.qzone.qq.com/1450136519')
req.add_header('cookie', 'pgv_pvi=5403712512; RK=g+9LmgrfRX; o_cookie=1450136519; pac_uid=0_8eb06a0d732fc; eas_sid=J115C1Q262x1t3c7X117s2y672; pgv_pvid=6941126393; ptcz=b319aa6f0c2ce3da846e28c330f468db6d1503a163ffa91ec63c32c0240d3be1; AMCV_A8023A875666943A7F000101%40AdobeOrg=1406116232%7CMCIDTS%7C17529%7CMCMID%7C87142526608295120981692136929186194928%7CMCAAMLH-1515136775%7C11%7CMCAAMB-1515136775%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1514539175s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C2.5.0%7CMCSYNCSOP%7C411-17537; pt2gguin=o1450136519; sd_userid=43441517988636180; sd_cookie_crttime=1517988636180; ptui_loginuin=1450136519; pgv_si=s2629840896; uin=o1450136519; pgv_info=ssid=s1404374000; qqmusic_fromtag=66; skey=@4aXN5x6HN; ptisp=cnc')
req.add_header('user-agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36')
resp = request.urlopen(req)
html= resp.read().decode('utf-8')
print(html)

def read_html():
	
	soup = BeautifulSoup(html,'html.parser')

	friends_list_soup = soup.find('li',attrs = {'class':'user-item'})

	return print(friends_list_soup)


read_html()
