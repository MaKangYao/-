import numpy as np

import pandas as pd

import matplotlib.pyplot as plt #1、拿画笔


#2、画布准备，画布可以隐式创建

plt.figure(figsize=(8,5))



#3、区域划分，sublot返回坐标系Axiues，默认111

plt.subplot(211) # 构建子图 21表示子图的排列2行1列，1表示放在第一个位置



# 4、设置坐标轴的范围 ，可以默认

plt.xlim(-10,10)

plt.ylim(-2,2)

# 设置坐标轴

plt.xlabel("自变量")

plt.ylabel("因变量")



x=np.arange(-5,5,0.1)

y=np.cos(x)

y1=np.sin(x)



#5、画画材料准备

#plot画折线，bar是柱状图，pie是饼图、scatter散点图

plt.plot(x,y,color="red",linestyle="dotted",linewidth=0.5,marker="*",label="余弦曲线")

plt.plot(x,y1,color="blue",linestyle="dashed",linewidth=1,marker="v",label='正弦曲线')

# 设置标题

plt.title("正弦余弦曲线")

# 显示图例，才能让lable显示到图形中

plt.legend()



#5、画画

plt.show()