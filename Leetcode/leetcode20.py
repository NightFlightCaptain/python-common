# -*- coding:utf-8 -*-
# @Time      :2018/11/19 14:44
# @Author    :wanhaoran
# @FileName  :leetcode20.py

"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

示例 1:

输入: "()"
输出: true
示例 2:

输入: "()[]{}"
输出: true
示例 3:

输入: "(]"
输出: false
示例 4:

输入: "([)]"
输出: false
示例 5:

输入: "{[]}"
输出: true
"""

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        c_map = {'(':')','[':']','{':'}'}
        stack = []
        for char in s:
            if char in "([{":
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                else:
                    cur_char = stack.pop()
                    if c_map[cur_char] != char:
                        return False
        if len(stack) == 0:
            return True
        else:return False


if __name__ == '__main__':
    print(Solution().isValid("{[[]()({[]})([])]}"))