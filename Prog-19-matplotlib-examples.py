# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.font_manager as fm
import matplotlib.pyplot as plt  

hzfont1 = fm.FontProperties(fname='C:\Windows\Fonts\simkai.ttf',size=16)
plt.figure(1,dpi=50)

# x轴的定义域，中间间隔100个元素  
x= np.linspace(-2*np.pi,2*np.pi,100) 
plt.plot(x,np.sin(x))

#设置X Y轴的文字
plt.xlabel("X")       
plt.ylabel("Y")
#设置图的标题  
plt.title("正弦函数",fontproperties=hzfont1)    
#显示图例
plt.legend()

plt.show()  
