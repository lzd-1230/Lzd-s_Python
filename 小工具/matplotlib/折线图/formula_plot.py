from matplotlib.legend import Legend
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
#指定默认字体
matplotlib.rcParams['font.sans-serif'] = ['SimHei'] 
matplotlib.rcParams['font.family']='sans-serif'
#解决负号'-'显示为方块的问题
matplotlib.rcParams['axes.unicode_minus'] = False

with open("./x.txt",mode="r") as f1,open("./y.txt",mode="r") as f2:
    x = f1.readline()
    x = [float(i) for i in x.split("\t")]
    y = f2.readline()
    y = [float(i) for i in y.split("\t")]
    
fig,ax = plt.subplots(figsize=(5,3),dpi=200)
fig.tight_layout()
ax = plt.gca()
ax.plot(x,y,label="实验数据")
x=np.linspace(0,1.6,50)
ax.plot(x,1740-20*x/0.126,label="理论计算")
ax.set_xlabel(r"转矩N·m")
ax.set_ylabel("转速r/min")
ax.legend()
plt.show()
fig.savefig("理论实际.png",bbox_inches = 'tight')