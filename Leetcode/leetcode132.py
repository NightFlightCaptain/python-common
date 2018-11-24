# -*- coding:utf-8 -*-
# @Time      :2018/11/24 13:41
# @Author    :wanhaoran
# @FileName  :leetcode132.py

"""
给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。

返回符合要求的最少分割次数。

示例:

输入: "aab"
输出: 1
解释: 进行一次分割就可将 s 分割成 ["aa","b"] 这样两个回文子串。
"""

class Solution:
    def minCut(self, s):
        """
        :type s: str
        :rtype: int

        可以进一步考虑将两个循环合并
        """
        length = len(s)
        dp = [[False] * length for i in range(length)]

        for i in range(length):
            for j in range(length):
                if j>=i:
                    dp[j][i]=True
                else:
                    if dp[j+1][i-1] and s[j]==s[i]:
                        dp[j][i]=True

        min_count = [i for i in range(length)]
        for i in range(1,length):
            for j in range(i+1):
                if dp[j][i]:
                    if j ==0:
                        min_count[i]=0
                        break
                    else:
                        min_count[i] = min(min_count[i],min_count[j-1]+1)
        return min_count[-1]






if __name__ == '__main__':
    solution = Solution()
    result = solution.minCut("aabc")
    print(result)