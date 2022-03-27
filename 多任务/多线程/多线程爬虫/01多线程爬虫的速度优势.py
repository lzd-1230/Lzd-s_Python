import time
import utils
import threading


def onethread_mode():
    for url in utils.urls:
        utils.spider(url)

def multi_mode():
    threads = []
    for url in utils.urls:
        threads.append(threading.Thread(target=utils.spider, args=(url,)))

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    start = time.time()
    multi_mode()
    print(f"耗时{round(time.time()-start, 2)}")


        
        