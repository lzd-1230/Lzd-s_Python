from pymysql import connect

def main():
    # 创建connect
    conn = connect(host="localhost",port=3306,user="root",password="112201",database="01-python",
                   charset="utf8")
    # 创建游标对象
    cs1 = conn.cursor()

    """ 通过cursor.execute("") 来执行sql语句"""


    # 关闭游标
    cs1.close()
    # 关闭connect
    conn.close()




if __name__ == "__main__":
    main()
