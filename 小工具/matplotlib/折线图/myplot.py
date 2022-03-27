from matplotlib.legend import Legend
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
#指定默认字体
matplotlib.rcParams['font.sans-serif'] = ['SimHei'] 
matplotlib.rcParams['font.family']='sans-serif'
#解决负号'-'显示为方块的问题
matplotlib.rcParams['axes.unicode_minus'] = False

"""拿到txt中的数据"""
def get_data(file_path):
    res = []
    with open(file_path,mode="r",encoding="gbk") as f:
        for line in f.readlines():
            res.append([float(i) for i in line.split("\t")]) 
        return res

"""绘制定制化的折线图"""
def plot_zhexian(x_titile,y_title,axes_title,legend:list):
    fig, ax = plt.subplots(figsize=(5,3),dpi=200)
    fig.tight_layout()
    ax.set_xlabel(x_titile)
    ax.set_ylabel(y_title)
    # 设置坐标轴
    ax = plt.gca()
    ax.spines["right"].set_visible(False) 
    ax.spines["top"].set_visible(False) 
    ax.spines["left"].set_position(("data", 0))
    ax.spines["bottom"].set_position(("data", 0))
    ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
    ax.plot(0, 0.99, "^k", transform=ax.get_xaxis_transform(), clip_on=False)
    ax.set_title(axes_title,fontsize=8)

    for idx,x in enumerate(x_all):
        y = y_all[idx]
        ax.plot(x,y,label=legend[idx],marker="o") # 绘图并设定legend
    
    ax.legend(fontsize=5, loc="lower right",)
    plt.show()
    fig.savefig("./test.png")

# 输入数据
x_all = get_data("./x.txt")
y_all = get_data("./y.txt")
plot_zhexian("s","T(N·m)","机械特性曲线",["电动运行","再生发电制动","反接制动","I=0.36A能耗制动","I=0.6A的能耗制动"])

