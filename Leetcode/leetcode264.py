# -*- coding:utf-8 -*-
# @Time      :2018/11/24 17:15
# @Author    :wanhaoran
# @FileName  :leetcode264.py


"""
编写一个程序，找出第 n 个丑数。

丑数就是只包含质因数 2, 3, 5 的正整数。

示例:

输入: n = 10
输出: 12
解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。
说明:

1 是丑数。
n 不超过1690。
"""
from collections import deque


class Solution:
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """

        # if n==1:
        #     return 1
        # q2,q3,q5=deque([2]),deque([3]),deque([5])
        # ugly_numbers =[1]
        # while n>1:
        #     x = min(q2[0],q3[0],q5[0])
        #     ugly_numbers.append(x)
        #     if x == q2[0]:
        #         q2.popleft()
        #         q2.append(x*2)
        #         q3.append(x*3)
        #         q5.append(x*5)
        #     if x == q3[0]:
        #         q3.popleft()
        #         q3.append(x*3)
        #         q5.append(x*5)
        #     if x == q5[0]:
        #         q5.popleft()
        #         q5.append(x*5)
        #     n-=1
        # return ugly_numbers[-1]

        if n ==1:
            return 1
        ugly_numbers =[1]
        i2,i3,i5=0,0,0
        for i in range(n-1):
            u2,u3,u5=2*ugly_numbers[i2],3*ugly_numbers[i3],5*ugly_numbers[i5]
            umin = min(u2,u3,u5)
            if umin==u2:
                i2+=1
            if umin==u3:
                i3+=1
            if umin==u5:
                i5+=1
            ugly_numbers.append(umin)
        return ugly_numbers[-1]

if __name__ == '__main__':
    solution = Solution()
    result = solution.nthUglyNumber(10)
    print(result)