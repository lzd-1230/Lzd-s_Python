from pymysql import connect

class JD(object):
    def __init__(self):
        pass
    def menu(self):
        print("-----查询服务列表-------")
        print("1:查询所有的学生")
        print("2:商品分类")
        print("3:品牌分类")
    def show_all_items(self):
        """ 展示所有的商品 """
        conn = connect(host="localhost",port=3306,password="112201",charset="utf8",database="01-python")
        cursor = conn.cursor()
        sql = "select * from students"
        cursor.execute(sql)
        for tmp in cursor.fetchall():
            print(tmp)
        cursor.close()
        conn.close()


    def run(self):
        while True:
            self.menu()
            num = input("请输入功能编号:")  # 这里没有用int转换,因为怕输入了其他的字母程序会崩

            if num == "1":
                self.show_all_items()
            elif num == "2":
                pass
            elif num == "3":
                pass
            else:
                print("输入有误,重新输入")




def main():
    # 创建一个对象
    service = JD()
    # 调用run方法,让他自己运行
    service.run()



if __name__ == "__main__":
    main()