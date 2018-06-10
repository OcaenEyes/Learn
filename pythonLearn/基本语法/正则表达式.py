''' 正则表达式是一个特殊的字符序列，一个字符串是否与我们所设定的字符序列相匹配
    快速检索文本、实现一些替换文本的操作
    1、检查一串数字是否是电话号码
    2、检测一个字符串是否符合额email
    3、把一个文本里指定的单词替换为另外一个单词
'''

import re

a = 'c|c++|Java|c#|Python|Javascript'
# print ('Python' in a )
r= re.findall('Python',a)
print(r)