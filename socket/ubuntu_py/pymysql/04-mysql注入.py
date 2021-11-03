from pymysql import connect

class JD(object):
    def __init__(self):
        self.conn = connect(host="localhost",port=3306,password="112201",charset="utf8",database="01-python")
        self.cursor = self.conn.cursor()

    @staticmethod
    def menu():
        print("-----查询服务列表-------")
        print("1:查询所有的学生")
        print("2:添加班级")
        print("3:查询学生姓名")

    def execute_sql(self,sql):
        self.cursor.execute(sql)
        for tmp in self.cursor.fetchall():
            print(tmp)

    def show_all_items(self):
        """ 展示所有的商品 """
        sql = "select * from students"
        self.execute_sql(sql)
    def get_info_by_name(self):
        find_name = input("请输入要查询的学生姓名:")
        sql = """select* from students where name = '%s';""" % find_name
        print("------------->%s<--------------" % sql)
        self.execute_sql(sql)

    def insert_class(self):
        name = input("请输入要添加的班级名称")
        sql = """insert into classes (name) values("%s")""" % name
        self.cursor.execute(sql)
        num = input("是否确定提交(y/n)?")
        if num == "y" or num == "Y":
            self.conn.commit()

    def run(self):
        while True:
            self.menu()
            num = input("请输入功能编号:")  # 这里没有用int转换,因为怕输入了其他的字母程序会崩

            if num == "1":
                self.show_all_items()
            elif num == "2":
                self.insert_class()
            elif num == "3":
                self.get_info_by_name()
            else:
                print("输入有误,重新输入")




def main():
    # 创建一个对象
    service = JD()
    # 调用run方法,让他自己运行
    service.run()



if __name__ == "__main__":
    main()
