# -*- coding: utf-8 -*-
# + {}
### 线条/条形和标记
#### 拉弧测试
import matplotlib.pyplot as plt 
import numpy as np 

def Test(t):
    a1 = np.cos(2 * np.pi * t)
    a2 = np.exp(-t)
    return a1 * a2 

b1 = np.arange(0.0,5.0,.2)

l = plt.plot(b1,Test(b1),'ro')
plt.setp(l,markersize=30)
plt.setp(l,markerfacecolor='C0')

plt.show()

# +
#### 堆积条形图
# yerr用于误差条的参数.
import numpy as np 
import matplotlib.pyplot as plt 

N = 5
menMeans = (20,35,30,35,27)
womenMeans = (25,32,34,20,25)
menStd = (2,3,4,1,2)
womenStd = (3,5,2,3,3)
ind = np.arange(N)
width = 0.35 

p1 = plt.bar(ind,menMeans,width,yerr=menStd)
p2 = plt.bar(ind,womenMeans,width,bottom=menMeans,yerr=womenStd)

plt.ylabel('Scores')
plt.title('Scores by group and gender')
plt.xticks(ind,('G1','G2','G3','G4','G5'))
plt.yticks(np.arange(0,81,10))
plt.legend((p1[0],p2[0]),('Men','Women'))

plt.show()

# +
#### 条形图
# 在单个条形图上带有误差条形图和高度标签.
import numpy as np 
import matplotlib.pyplot as plt 

men_means,men_std = (20,35,30,35,27),(2,3,4,1,2)
women_means,women_std = (25,32,34,20,25),(3,5,2,3,3)

ind = np.arange(len(men_means))
width = 0.35 

fig,ax = plt.subplots()
rects1 = ax.bar(ind - width/2, men_means,width,
                yerr=men_std,color='SkyBlue',label='Men')
rects2 = ax.bar(ind + width/2,women_means,width,yerr=women_std,
               color='IndianRed',label='Women')

ax.set_ylabel('Scores')
ax.set_title('Scores by group and gender')
ax.set_xticks(ind)
ax.set_xticklabels(('G1','G2','G3','G4','G5'))
ax.legend()


def Autolabel(rects,xpos='center'):
    
    xpos = xpos.lower()
    ha = {'center':'center','right':'left','left':'right'}
    offset = {'center':0.5,'right':0.57,'left':0.43}
    
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()*offset[xpos],
                1.01*height,'{}'.format(height),ha=ha[xpos],va='bottom')
        

Autolabel(rects1,"left")
Autolabel(rects2,"right")
plt.show()
# + {}
#### 水平条形图
import matplotlib.pyplot as plt 
import numpy as np 

np.random.seed(20190825)

plt.rcdefaults()
fig,ax = plt.subplots()

people = ('Tom','Dick','Harry','Slim','Jim')
y_pos = np.arange(len(people))
performance = 3 + 10 * np.random.rand(len(people))
error = np.random.rand(len(people))

ax.barh(y_pos,performance,xerr=error,align='center',
       color='green',ecolor='black')
ax.set_yticks(y_pos)
ax.set_yticklabels(people)
ax.invert_yaxis()
ax.set_xlabel('Performance')
ax.set_title('How fast do you want to go today?')
plt.show()

