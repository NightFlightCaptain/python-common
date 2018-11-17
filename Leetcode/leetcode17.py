# -*- coding:utf-8 -*-
# @Time      :2018/11/17 21:57
# @Author    :wanhaoran
# @FileName  :leetcode17.py

class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        def combination(already_result,single_digit):
            c = []
            for i in lookup[single_digit]:
                if len(already_result) == 0:
                    c.append(i)
                else:
                    for j in already_result:
                        c.append(j+(i))
            return c

        lookup = {
            '2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z']
        }

        reslut = []

        for i in digits:
            reslut = combination(reslut,i)
        return reslut


if __name__ == '__main__':
    print(Solution().letterCombinations("233"))