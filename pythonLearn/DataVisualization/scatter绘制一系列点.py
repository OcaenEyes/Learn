import matplotlib.pyplot as plt
# x_value = [1,2,3,4,5]
# y_value = [1,4,9,16,25]

# plt.scatter(x_value,y_value,s=100)
x_value= list(range(1,1001))
y_value = [x**2 for x in x_value]
#删除数据点的轮廓
plt.scatter(x_value,y_value,c='red',edgecolor ='none',s = 40)

plt.axis([0,1100,0,1100000])

plt.show()