import flask
import math
import json
from concurrent.futures import ProcessPoolExecutor

app = flask.Flask(__name__)

def is_prime(n):
    if n<2:
        return False
    if n == 2:
        return True
    if n%2 == 0:
        return False
    sqrt_n = int(math.floor(math.sqrt(n)))

    for i in range(3, sqrt_n+1,2):
        if n%i == 0:
            return False
    return True

@app.route("/is_prime/<nums>")
def cak(nums):
    print(f"进入到了该服务中,参数为{nums}")
    number_list = [int(x) for x in str(nums).split(",")]
    print(number_list)
    results = process_pool.map(is_prime, number_list)
    ret = json.dumps(
            dict(zip(number_list,results))
            )
    return ret # 这种函数注意一定要有返回值

if __name__ == "__main__":
    process_pool = ProcessPoolExecutor() # 注意进程池一定要定义在主函数中,而线程池可以定义在全局变量的位置
    app.run()


