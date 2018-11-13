# -*- coding:utf-8 -*-
# __author__ = 'wanhaoran'

"""
与map的区别，namedtuple中的值是不能改变的
"""
from collections import namedtuple

Friend = namedtuple("a1111",['name','age','email'])
friend1 = Friend("wangxiaoming",16,"wangxiaoming@163.com")
print(friend1.name)
# friend1.name = "lixiaoming" #报错
