# _*_ coding:utf-8 _*_
import sys
import io 
import os
import itchat
import PIL.Image as Image
from os import listdir
import math

# 登录
itchat.auto_login()

friends = itchat.get_friends(update = True)[0:]
print(type(friends))
# print(friends)

user = friends[0]['UserName']
print(user)

os.mkdir(user)
num = 0 
x = 0 
y =0
for i in friends:
    img = itchat.get_head_img(userName = i['UserName']) 
    fileImage = open(user + '/' + str(num) + '.jpg','wb')
    fileImage.write(img)
    fileImage.close()
    num = num+1


pics = listdir(user)
print(pics)
numPic = len(pics)
print(numPic)

eachsize = int(math.sqrt(float(1280*1280)/ numPic))

print(eachsize)
numline = int(1280/eachsize)

toImage = Image.new('RGBA',(1280,1280))

print(numline)

for i in pics:
	try:
		img = Image.open(user + '/' + i)
	except IOError:
		print('Error:没有找到文件或读取文件失败')
	else:
		img= img.resize((eachsize,eachsize), Image.ANTIALIAS)
		toImage.paste(img,(x*eachsize,y*eachsize))
		x= x+1
		if x== numline:
			x= 0
			y =y+1


toImage.save(user + '.BMP')
