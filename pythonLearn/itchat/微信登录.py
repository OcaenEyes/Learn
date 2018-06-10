# _*_ coding:utf-8 _*_

import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

print('itchat 爬取微信')

import itchat


# 微信网页登录
itchat.auto_login()

# 微信传输助手的运用
itchat.send('Hello, 乔克叔叔',toUserName='filehelper')