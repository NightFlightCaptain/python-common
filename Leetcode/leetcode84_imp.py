# -*- coding:utf-8 -*-
# @Time      :2018/11/19 17:29
# @Author    :wanhaoran
# @FileName  :leetcode84_imp.py

"""
给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。

求在该柱状图中，能够勾勒出来的矩形的最大面积。

以上是柱状图的示例，其中每个柱子的宽度为 1，给定的高度为 [2,1,5,6,2,3]。

图中阴影部分为所能勾勒出的最大矩形面积，其面积为 10 个单位。

示例:

输入: [2,1,5,6,2,3]
输出: 10
"""


class Solution:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """

        """
        
        第一种解法
        left_indexes = [-1] * len(heights)
        right_indexes = [len(heights)] * len(heights)
        left_stack, right_stack = [], []

        for i in range(len(heights)):
            while right_stack and heights[i] < heights[right_stack[-1]]:
                right_indexes[right_stack.pop()] = i
            right_stack.append(i)

        for i in range(len(heights)-1,-1,-1):
            while left_stack and heights[i] < heights[left_stack[-1]]:
                left_indexes[left_stack.pop()] = i
            left_stack.append(i)

        res = 0
        for i in range(len(heights)):
            res = max(heights[i]*(right_indexes[i]-left_indexes[i]-1),res)
        return res
        """

        area,stack = 0,[-1]
        heights.append(0)  # 保证heights中的值得到计算
        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:  # heights[-1]刚好又等于0
                h = heights[stack.pop()]
                w = i - stack[-1] -1
                area = max(area,h*w)
            stack.append(i)
        return area

if __name__ == '__main__':
    print(Solution().largestRectangleArea([2, 1, 5, 6, 2, 3]))
