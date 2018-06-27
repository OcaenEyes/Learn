import sys
import io 
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding= 'utf-8')

import matplotlib.pyplot as plt

plt.scatter(2,4,s=200)
#设置图表标题，并给坐标轴加上标签
plt.title('Square Numbers',fontsize = 24)
plt.xlabel('Value',fontsize = 14)
plt.ylabel('Square of value', fontsize= 14)

plt.tick_params(axis='both',which = 'major',labelsize = 14)
plt.show()