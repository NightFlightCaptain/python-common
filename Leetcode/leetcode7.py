# -*- coding:utf-8 -*-
# __author__ = 'wanhaoran'

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        if x >=0:
            result = int(str(x)[::-1])
        else:
            result = int('-'+str(-x)[::-1])
        if result >= 2**31-1 or result<=-2**31:
            result = 0
        return result

if __name__ == '__main__':
    print(2**31-1)
    print(Solution().reverse(1534236469))