# -*- coding:utf-8 -*-
# __author__ = 'wanhaoran'

"""
问题：
定义一个int型的一维数组，包含40个元素，用来存储每个学员的成绩，循环产生40个0~100之间的随机整数，
(1)将它们存储到一维数组中，然后统计成绩低于平均分的学员的人数，并输出出来。
(2)将这40个成绩按照从高到低的顺序输出出来。
"""

import random

def make_score(num):
    scores = [random.randint(0,100) for i in range(num)]
    return scores

def less_average(score):
    average_score = sum(score)/len(score)
    count = 0
    for i in range(len(score)):
        if score[i] < average_score:
            count+=1

    # less_ave = [i for i in score if i<average_score]
    return average_score,count


if __name__=="__main__":
    score = make_score(40)
    average_num,less_num = less_average(score)
    print('the score of average is:',average_num)
    print("the number of less average is:",less_num)
    print("the every score is[from big to small]:",sorted(score,reverse=True))