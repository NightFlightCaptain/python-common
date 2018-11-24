# -*- coding:utf-8 -*-
# @Time      :2018/11/24 15:49
# @Author    :wanhaoran
# @FileName  :leetcode221.py


"""
在一个由 0 和 1 组成的二维矩阵内，找到只包含 1 的最大正方形，并返回其面积。

示例:

输入:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

输出: 4


"""
"""
该题目有leetcode84、leetcode85有联系
"""


class Solution:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or len(matrix)==0:
            return 0

        row = len(matrix)
        col = len(matrix[0])
        dp=[[int(matrix[i][j]) for j in range(col)] for i in range(row)]

        for i in range(1,row):
            for j in range(1,col):
                if dp[i][j] ==1:
                    dp[i][j] = min(dp[i-1][j-1],dp[i][j-1],dp[i-1][j])+1

        max_area = 0
        for i in dp:
            for j in i:
                max_area = max(max_area,j**2)
        return max_area

if __name__ == '__main__':
    solution = Solution()
    result = solution.maximalSquare(

        [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]])
    print(result)
