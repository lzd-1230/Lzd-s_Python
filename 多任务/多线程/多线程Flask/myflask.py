import flask
import time
import json
from concurrent.futures import ThreadPoolExecutor,as_completed

"""
用sleep去模拟IO操作,然后用线程池去优化
    不优化的结果:0.65s左右
    优化的结果:0.31s左右
最终的消耗时间取决于最慢的那个任务运行消耗的时间.
"""

app = flask.Flask(__name__)
pool = ThreadPoolExecutor() # 创建一个全局得线程池

def read_file():
    time.sleep(0.1)
    return "file"

def read_db():
    time.sleep(0.2)
    return "db"

def read_api():
    time.sleep(0.3)
    return "api"

@app.route("/")
def index():
    result_file = pool.submit(read_file) # 创建线程
    result_db = pool.submit(read_db)
    result_api = pool.submit(read_api)

    return json.dumps(
        {
            "result_file": result_file.result(), # 获取线程执行得结果
            "result_db": result_db.result(),
            "result_api": result_api.result()
        }
    )


if __name__ == "__main__":
    app.run()