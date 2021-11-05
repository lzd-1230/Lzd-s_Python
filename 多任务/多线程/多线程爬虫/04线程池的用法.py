from concurrent import futures
from concurrent.futures import ThreadPoolExecutor,as_completed
import utils

print("map 的方式")
# 模板一:
with ThreadPoolExecutor() as pool:
    htmls = pool.map(utils.spider,utils.urls)
    results = list(zip(utils.urls, htmls))

    for url,html in results:
        print(url, len(html))

print("sumbmit 的方式")
# 模板二:
with ThreadPoolExecutor() as pool:
    futures_dict = {}
    # futures = [pool.submit(utils.spider,url) # 线程列表,但是这里可以构建一个字典结构把url和线程对应
    #            for url in utils.urls]
    # 构造线程字典
    for url,html in results:
        future = pool.submit(utils.parse, html)
        futures_dict[future] = url # 因为等会用as_complete遍历的时候,对字典只能遍历键值
    
    # 严格按照urls的顺序返回
    # for url, future in futures_dict.items():
        # print(url, future.result())

    # 按照完成的顺序返回
    for feature in as_completed(futures_dict):
        url = futures_dict[feature]
        print(url, feature.result())

    
    
