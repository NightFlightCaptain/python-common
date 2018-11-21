# -*- coding:utf-8 -*-
# @Time      :2018/11/21 14:01
# @Author    :wanhaoran
# @FileName  :leetcode96.py

"""
给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？

示例:

输入: 3
输出: 5
解释:
给定 n = 3, 一共有 5 种不同结构的二叉搜索树:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""


class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """

        """
        递归超时
        if n <=0:
            return 1
        res = 0
        for i in range(1,n+1):
            res+=self.numTrees(i-1)*self.numTrees(n-i)
        return res
        """
        if n <=0:
            return 1
        dp = [0 for i in range(n+1)]
        dp[0],dp[1]=1,1
        for i in range(2,n+1):
            for j in range(i):
                dp[i] += dp[j]*dp[i-j-1]
        return dp[-1]

if __name__ == '__main__':
    print(Solution().numTrees(3))