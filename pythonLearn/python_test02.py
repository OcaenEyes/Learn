#!/usr/bin/python3
# -*- coding:utf-8 -*-
'''
	date:2018-06-02
	version:0.1.0
'''
import sys
import io

# 设置输出模式为UTF-8
sys.stdout =  io.TextIOWrapper(sys.stdout.buffer,encoding = 'utf-8')

# 题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
print('题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？')
# 题目分析
# 可在 个，十，百上的数字全排列，排除重复的组合
# 初始化计数
n = 0
# 遍历从1到5，但不包括5
for i in range(1,5):
	for j in range(1,5):
		for k in range(1,5):
			if (i!=j) and (i != k) and (j != k):
				print(i,j,k)
				n= n+1       #计数+1

# 输出计数结果
print(n)

 