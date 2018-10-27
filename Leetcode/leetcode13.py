# -*- coding:utf-8 -*-
# __author__ = 'wanhaoran'

class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        numList = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
        romanList = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']

        l = len(numList) -1
        num = 0
        while l >=0:
            while s.startswith(romanList[l]):
                num+=numList[l]
                s=s[len(romanList[l]):]
            l-=1
        return num

if __name__ == '__main__':
    print(Solution().romanToInt("MCMXCIV"))