# -*- coding:utf-8 -*-
# __author__ = 'wanhaoran'

class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        numList = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
        romanList = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']
        l = len(numList)-1
        str = ''
        while l >=0:
            while num>=numList[l]:
                str+=romanList[l]
                num-=numList[l]
            l-=1
        return str


if __name__ == '__main__':
    print(Solution().intToRoman(1994))
