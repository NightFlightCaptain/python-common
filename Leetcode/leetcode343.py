# -*- coding:utf-8 -*-
# @Time      :2018/12/14 14:05
# @Author    :wanhaoran
# @FileName  :leetcode343.py

"""
Given a positive integer n, break it into the sum of at least two positive integers and maximize the product of those integers. Return the maximum product you can get.

Example 1:

Input: 2
Output: 1
Explanation: 2 = 1 + 1, 1 × 1 = 1.
Example 2:

Input: 10
Output: 36
Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.
Note: You may assume that n is not less than 2 and not larger than 58.
"""
import math


class Solution:
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        cache = [1] *(n+1)
        for i in range(2,n+1):
            for j in range(1,i):
                cache[i] = max(cache[i],j*(i-j),j*cache[i-j])
        return cache[-1]

if __name__ == '__main__':

    solution = Solution()
    result = solution.integerBreak(10)
    print(result)