"""
本脚本实现通过命令行来上传.csv文件至mysql中
    但是目前对于大的csv无能为力
    且mysql的端口和ip也是写死了的
"""
import pandas as pd
import re
import pymysql
import copy
import argparse

# 全局
parser = argparse.ArgumentParser()


"""连接数据库"""
def connect_to_db(db_name):
    conn = pymysql.connect(host="121.4.162.140",port=33333,user='root',passwd='123456',db=db_name,charset='utf8')
    cursor = conn.cursor()
    print("数据库成功连接")
    return conn,cursor
    Exc


def sql_deal(sql,line):
    for idx,elem in enumerate(line):
        # 非最后一个元素
        if(idx < len(line) - 1):
            if(type(elem) == str):
                sql = sql + '"' + elem + '"' + ","
            else:
                sql = sql + str(elem) + ","
        else:
            if(type(elem) == str):
                sql = sql + '"' + elem + '"'
            else:
                sql = sql + str(elem)
            sql = sql + ");"
    return sql

"""完成csv数据的输入"""
def insert_to_table(db_name,table_name,csv_df):
    conn, cursor = connect_to_db(db_name)
    counts = 0
    table_judge(cursor,table_name,csv_df)
    for line in csv_df.values:
        sql = 'insert into '+ table_name +' values('
        # 对每一条数据进行处理变成sql语句的形式插入
        sql = sql_deal(copy.deepcopy(sql),line) 
        counts += 1
        # 执行sql语句
        cursor.execute(sql)
        conn.commit()
    print(f"共添加了{counts}条数据")

def table_judge(cursor,table_name,table_df):
    # 查询表是否存在
    sql = "show tables;"
    cursor.execute(sql)
    search = list(cursor.fetchall())
    # 提取获取到的信息
    search_list = re.findall('(\'.*?\')',str(search))
    search_list = [re.sub("'",'',each)for each in search_list]
    if(table_name in search_list):
        print("找到数据表")
    else:
        print("创建表")
        columns = table_df.columns
        columns_type = type_map(table_df)
        print(columns)
        print(columns_type)
        table_columns_type = ",".join(["`"+elem[0]+"`"+f" {elem[1]}" for elem in zip(columns,columns_type)])
        sql = f"create table {table_name} ({table_columns_type});"
        print(sql)
        # cursor.execute(sql)

def type_map(csv_df):
    """将csv的列的数据类型,转换至mysql中"""
    colunms = csv_df.columns
    columns_type = [str(csv_df[col].dtype) for col in colunms]
    for idx,col_type in enumerate(columns_type):
        if(col_type.startswith("float")):
            columns_type[idx] = "float"
        elif(col_type.startswith("int")):
            columns_type[idx] = "int"
        elif(col_type.startswith("object")):
            columns_type[idx] = "varchar(20)"
    return columns_type

def test_func():
    conn, cursor = connect_to_db("mydb")
    table_judge(cursor,"xxx",csv_df)
    insert_to_table("mydb","test",csv_df)

def arg_init():
    parser.add_argument("-t",help="指定表名",type=str)
    parser.add_argument("-d",help="指定数据库",type=str)
    

if __name__ == "__main__":
    arg_init()
    args = parser.parse_args()
    insert_to_table(args.d,args.t,csv_df)
