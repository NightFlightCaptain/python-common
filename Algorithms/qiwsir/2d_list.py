# -*- coding:utf-8 -*-
# __author__ = 'wanhaoran'

import random

"""
问题
定义一个20*5的二维数组，用来存储某班级20位学员的5门课的成绩；这5门课按存储顺序依次为：core C++，coreJava，Servlet，JSP和EJB。
（1）循环给二维数组的每一个元素赋0~100之间的随机整数。
（2）按照列表的方式输出这些学员的每门课程的成绩。
（3）要求编写程序求每个学员的总分，将其保留在另外一个一维数组中。
（4）要求编写程序求所有学员的某门课程的平均分。
"""
def score(score_student_list,course_list,student_num):
    course_num=len(course_list)
    student_score_list = [[score_list[i][j] for i in range(course_num)] for j in range(student_num)]

    # 每门课程的总分
    course_ave_list = [sum(score_list[i]) for i in range(course_num)]

    # 每个学生的总分
    every_student_total_list = [sum(student_score_list[i]) for i in range(student_num)]

    return course_ave_list,every_student_total_list

if __name__ == '__main__':
    course_list = ["C++","Java","Servlet","JSP","EJB"]
    student_num = 20
    score_list = [[random.randint(0,100) for i in range(student_num)] for j in range(len(course_list))]
    score(score_list,course_list,student_num)
    for i in range(len(score_list)):
        print(score_list[i])
    course_ave_list, every_student_total_list = score(score_list,course_list,student_num)
    for i in range(len(course_list)):
        print("the ave of ",course_list[i],": ",course_ave_list[i])
    for i in range(student_num):
        print("第",i,"个学生的总分： ",every_student_total_list[i])