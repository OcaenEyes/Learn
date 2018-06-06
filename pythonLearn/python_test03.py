# _*_ coding:utf-8 _*_
import sys
import io

# 设置输出模式为UTF-8
sys.stdout =  io.TextIOWrapper(sys.stdout.buffer,encoding = 'utf-8')

print('题目：企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于40万元的部分，可提成3%；60万到100万之间时，高于60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？')
# 题目分析
# 区分利润区间，对应该区间的分成占比
# 可利用列表，设置区间
# 用净利润减去列表对应区间的阈值

# 输入净利润
i = int(input('净利润：'))
print('净利润',i)


# 利润区分阶段
lirun_arr = [1000000,600000,400000,200000,100000,0]

# 提成区分阶段
ticheng_arr = [0.01,0.015,0.03,0.05,0.075,0.1]
# 初始化提成
r = 0

for idx in range(0,6):
	lirun = int(lirun_arr[idx])
	print('净利润区间',lirun)
	if (i >lirun):
		print('该区间提成',(i -lirun)*(ticheng_arr[idx]))
		r= r+ (i - lirun)* (ticheng_arr[idx])
		i = lirun     #重新赋值

print('总提成',r)

