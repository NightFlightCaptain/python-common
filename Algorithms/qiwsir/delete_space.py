# -*- coding:utf-8 -*-
# __author__ = 'wanhaoran'

"""
删除一个字符串中连续超过一次的空格。
"""


def del_space(string):
    string_split = string.split(' ')
    print(string_split)

    string_list = [string_split[0]]
    for i in range(1,len(string_split)):
        if string_split[i] !='':
            if string_split[i-1] !='':
                string_list.append(" ")
        string_list.append(string_split[i])

    string_result="".join(string_list)
    return string_result

print(del_space("a  bb               c"))
