# -*- coding:utf-8 -*-
# __author__ = 'wanhaoran'


class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x % 10 == 0 and x !=0):
            return False
        revertedNum = 0
        while(x > revertedNum):
            revertedNum = revertedNum * 10+x%10
            x//=10
        return x==revertedNum or x==revertedNum//10


if __name__ == '__main__':
    print(Solution().isPalindrome(1011))