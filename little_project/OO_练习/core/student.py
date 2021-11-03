from lib import common



def stu_register():
    pass


@common.auth("Student")
def check_score():
    pass

@common.auth("Student")
def choose_lesson():
    pass


def student_view():
    while True:
        print(
            '''
          =====学生面板======  
            1.学生注册
            2.查看分数
            3.选课
            '''
        )
        choice = input("请输入功能:")


stu_fun_dict = {
    "1":stu_register,
    "2":check_score,
    "3":choose_lesson
}
