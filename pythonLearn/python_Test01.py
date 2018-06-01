#!/usr/bin/python3
#-*- coding:UTF-8 -*-
import sys
import locale
import io
import os
import codecs
print(sys.getdefaultencoding()+" - sys.getdefaultencoding")

print(sys.stdout.encoding + " - sys.stout.encoding")

# 改变标准输出的默认编码
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding = 'utf-8')

a = '测试'
b = u'测试'
print (a)
print (b) 