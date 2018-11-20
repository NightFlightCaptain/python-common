# -*- coding:utf-8 -*-
# @Time      :2018/11/19 16:39
# @Author    :wanhaoran
# @FileName  :leetcode72.py

"""
给定两个单词 word1 和 word2，计算出将 word1 转换成 word2 所使用的最少操作数 。

你可以对一个单词进行如下三种操作：

插入一个字符
删除一个字符
替换一个字符
示例 1:

输入: word1 = "horse", word2 = "ros"
输出: 3
解释:
horse -> rorse (将 'h' 替换为 'r')
rorse -> rose (删除 'r')
rose -> ros (删除 'e')
示例 2:

输入: word1 = "intention", word2 = "execution"
输出: 5
解释:
intention -> inention (删除 't')
inention -> enention (将 'i' 替换为 'e')
enention -> exention (将 'n' 替换为 'x')
exention -> exection (将 'n' 替换为 'c')
exection -> execution (插入 'u')
"""

class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        len_word1 = len(word1)
        len_word2 = len(word2)
        dp = [[0]*(len_word1+1) for i in range(len_word2+1)]
        for i in range(len_word1+1):
            dp[0][i] = i
        for j in range(len_word2+1):
            dp[j][0] = j
        for i in range(1,len_word2+1):
            for j in range(1,len_word1+1):

                if word2[i-1] == word1[j-1]:
                    dp[i][j]= dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
                    # if i==j:
                    #     dp[i][j] = min(dp[i][j],i)
        return dp[-1][-1]


if __name__ == '__main__':
    print(Solution().minDistance("mart","karma"))