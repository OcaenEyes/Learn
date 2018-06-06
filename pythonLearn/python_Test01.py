# _*_ coding:UTF-8 _*_
import sys
import locale
import io
import os
import codecs
print(sys.getdefaultencoding()+" - sys.getdefaultencoding")

print(sys.stdout.encoding + " - sys.stout.encoding")

# 改变标准输出的默认编码
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding = 'utf-8')
# 输出模式修改为UTF-8，则可print中文
print(sys.stdout.encoding)

a = '测试'
b = '测试'
print (a)
print (b) 