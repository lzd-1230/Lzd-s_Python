from tkinter import *
import subprocess
import threading
import time
import re

# 当按件被按下后的槽函数
def btn_click():
    text.insert(INSERT, ("IP地址        状态!\n"))
    i = 0
    j = 1
    thread_id = []
    ip = int(ipText.get())
    # 构造待检测的ip生成器
    v = ('192.168.1.%d' % (x) for x in range(1, ip + 1))
    print(v)
    for it in v:
        loop = str('%s' % it)
        thread_id.append(0)
        thread_id[i] = Ping(loop, int(j / 20))
        thread_id[i].start()
        # thread_id[i].join()
        i = i + 1
        j = j + 10

# 完成ping命令的线程
class Ping(threading.Thread):
    def __init__(self, str_ip, sleep_time):
        threading.Thread.__init__(self)
        self.str_ip = str_ip
        self.sleep_time = sleep_time

    def run(self):
        time.sleep(self.sleep_time) # ??为啥要睡??
        # 执行ping命令
        ftp_ret = subprocess.Popen('ping %s -n 3' % self.str_ip, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                   shell=True)
        # 拿到输出结果
        ret = ftp_ret.stdout.read()
        str_ret = ret.decode("gbk")
        ret_s = re.search("TTL", str_ret)
        if ret_s:
            text.insert(INSERT, ("%s    在线!\n" % self.str_ip))
            # text.update()
        else:
            pass
            # text.insert(INSERT, ("%s    下线!\n" % self.str_ip))

root = Tk()
root.title('局域网Ping程序')
root.geometry('600x400')
main_frame = Frame(root)
text_frame = Frame(main_frame)
ip_frame = Frame(main_frame)
botton_frame = Frame(ip_frame)

l1 = Label(ip_frame, text='IP地址：192.168.10 从 0 到')
l2 = Label(ip_frame, text='   线程20   ')
ipText = Entry(ip_frame)

l1.pack(side='left')
ipText.pack(side='left')
ipText['width'] = 5
l2.pack(side='left')
b = Button(ip_frame, text='开始', command=btn_click)
b['width'] = 4
b['height'] = 1
b.pack(side='left')

# 文字显示区
text = Text(text_frame, width=30, height=25)
text.pack()
main_frame.pack()
ip_frame.pack(side='top', pady='5')
text_frame.pack()
root.mainloop()