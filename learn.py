import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm #导入字体管理包

# myfont=fm.fontproperties(fname=r'C:\Windows\Fonts\simsun.ttf')
# 理论说导入以后就可以用字体的名字来放到fontproperties里面去了，没有测试过，因为宋体就足够使用了
x=np.arange(0,2.0*np.pi,0.1)
y=np.cos(x)
plt.scatter(x,y,s=50,linewidths=6,marker='*',c='#FFAF37')
plt.xlabel('x-变量宋体')

plt.xlabel("x-变量",fontproperties='SimHei') #这里利用了参数强行改变了字体
plt.ylabel("y-变量",fontproperties='fangsong',fontsize=18) #这种方法最恰当，可以很好的显示中文，还能够防止英文字符的错乱
plt.title('大屁股裂了尼玛死',fontproperties='Simsun',fontsize='18')
#已知可用字体 Simsun（宋体） Kaiti fangsong simhei（微软雅黑？）等

plt.show()