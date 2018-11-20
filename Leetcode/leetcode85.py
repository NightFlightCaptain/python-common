# -*- coding:utf-8 -*-
# @Time      :2018/11/19 17:19
# @Author    :wanhaoran
# @FileName  :leetcode85.py

"""
给定一个仅包含 0 和 1 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。

示例:

输入:
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
输出: 6
"""

"""
参照leetcode84可以解答
"""


class Solution:
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """

        def largestRectangleArea(heights):

            left_indexes, right_indexes = [-1] * len(heights), [len(heights)] * len(heights)
            left_stack, right_stack = [], []
            for i in range(len(heights)):
                while right_stack and heights[i] < heights[right_stack[-1]]:
                    right_indexes[right_stack.pop()] = i
                right_stack.append(i)

            for i in range(len(heights) - 1, -1, -1):
                while left_stack and heights[i] < heights[left_stack[-1]]:
                    left_indexes[left_stack.pop()] = i
                left_stack.append(i)

            res = 0
            for i in range(len(heights)):
                res = max(res,(right_indexes[i]-left_indexes[i] -1)*heights[i])
            return res

        if not matrix or not matrix[0]:
            return 0
        heights = [0 for i in range(len(matrix[0]))]
        max_area = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == '1':
                    heights[j] += 1
                else:
                    heights[j]=0
            max_area = max(max_area,largestRectangleArea(heights))

        return max_area



if __name__ == '__main__':
    print(Solution().maximalRectangle([

    ]))
