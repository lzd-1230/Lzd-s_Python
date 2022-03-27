import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from scipy.optimize import curve_fit

#指定默认字体
matplotlib.rcParams['font.sans-serif'] = ['SimHei'] 
matplotlib.rcParams['font.family']='sans-serif'
#解决负号'-'显示为方块的问题
matplotlib.rcParams['axes.unicode_minus'] = False
x = [100,200,300,400,500,600,700]
x = np.array(x)

y = [0.03,0.17,0.43,0.78,1.24,1.79,2.43]
y = np.array(y)

fun = np.polyfit(x,y,1)
print(fun)

figure = plt.figure(dpi=200)
plt.scatter(x,y)
x = np.arange(0.0,700,0.1)
y = 0.00401786*x - 0.62571429
plt.plot(x,y)
plt.xlabel("温度" + r"$°C$")
plt.ylabel("热电偶电压" + r"$mV$")
plt.savefig("./test.png",bbox_inches = 'tight')
plt.show()