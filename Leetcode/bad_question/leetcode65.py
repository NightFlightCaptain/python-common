# -*- coding:utf-8 -*-
# @Time      :2018/11/19 14:20
# @Author    :wanhaoran
# @FileName  :leetcode65.py

"""
验证给定的字符串是否为数字。

例如:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true

说明: 我们有意将问题陈述地比较模糊。在实现代码之前，你应当事先思考所有可能的情况。

更新于 2015-02-10:
C++函数的形式已经更新了。如果你仍然看见你的函数接收 const char * 类型的参数，请点击重载按钮重置你的代码。
"""


class Solution:
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip()
        if s.find('e') != -1 or s.find('.')!=-1:
            if s.find('e') != -1:
                str_ = s.split("e")
                if len(str_) != 2:
                    return False
                else:
                    if str_[0].isdigit() and str_[1].isdigit():
                        return True
                    else:
                        return False
            else:
                str_ = s.split(".")
                if len(str_) > 2:
                    return False
                else:
                    for i in str_:
                        if i!= '' and not i.isdigit():
                            return False
                    return True
        if s.isdigit():
            return True
        else:return False

if __name__ == '__main__':
    print(Solution().isNumber("100."))
    # print("0.1".isdigit())
    print(10.)
