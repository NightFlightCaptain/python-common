# -*- coding:utf-8 -*-
# __author__ = 'wanhaoran'

"""
删除一个字符串中连续超过一次的空格。
"""


def del_space(string):
    string_split = string.split(' ')
    print(string_split)

    # string_new = [i for i in string_split if i !=""]
    # print(string_new)

    string_split.remove("")
    string_result=" ".join(string_split)
    return string_result


print(del_space("a bb  c"))
