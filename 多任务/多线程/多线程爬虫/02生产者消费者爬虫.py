import queue
import utils
import time
import threading
import random

def do_spider(url_queue:queue.Queue, html_queue:queue.Queue):
    while True:
        # 从队列里获得一个url
        url = url_queue.get() 
        # 进行爬取
        html_res = utils.spider(url)
        # 向html队列中添加
        html_queue.put(html_res)
        # 打印日志
        print(threading.current_thread().name, f"spider{url}","que_size=",html_queue.qsize())
        time.sleep(random.randint(1,2))

def do_store(html_queue:queue.Queue,fout):
    while True: # 这个作用是防止该线程结束从而导致文件未写入成功
        # 将队列中的内容写入文件
        html = html_queue.get() 
        # 拿到解析后的结果
        results = utils.parse(html) 
        # print(results)
        # 保存到文件中
        for result in results:
            fout.write(str(result) + "\n")
        print(threading.current_thread().name, f"store {url}",f"results_size={len(results)}")
        time.sleep(random.randint(1,2))

if __name__ == "__main__":
    url_queue = queue.Queue()
    html_queue = queue.Queue()

    for url in utils.urls:
        url_queue.put(url)

    for idx in range(3):
        t = threading.Thread(target=do_spider, args=(url_queue, html_queue), 
                             name = f"spider{idx}")
        t.start()

    fout = open("02data.txt",mode ="w",encoding="utf-8")

    for idx in range(3):
        t = threading.Thread(target=do_store, args=(html_queue, fout), 
                                name = f"store{idx}")
        t.start()