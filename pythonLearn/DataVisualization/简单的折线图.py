import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
import matplotlib.pyplot as plt
# 平方数
squares = [1,4,9,16,25]
input_values = [1,2,3,4,5]
plt.plot(input_values,squares,linewidth= 5)

# 设置图标标题，并给坐标轴加上标签
plt.title('squares number',fontsize = 24)

plt.xlabel('value',fontsize=14)

plt.ylabel('squares value',fontsize= 14)

plt.tick_params(axis= 'both',labelsize =14)

plt.show()
