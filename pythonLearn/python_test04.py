# _*_ coding:utf-8 _*_
'''
    auth:gzy
    version:0.1.0
    date:2018-06-05
'''
import io
import sys
#改变标准输出的默认编码
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')

print('题目：输入某年某月某日，判断这一天是这一年的第几天？程序分析：以3月5日为例，应该先把前两个月的加起来，然后再加上5天即本年的第几天，特殊情况，闰年且输入月份大于2时需考虑多加一天：')