# -*- coding:utf-8 -*-
# @Time      :2018/11/21 15:49
# @Author    :wanhaoran
# @FileName  :leetcode120.py


"""
给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。

例如，给定三角形：

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。

说明：

如果你可以只使用 O(n) 的额外空间（n 为三角形的总行数）来解决这个问题，那么你的算法会很加分。
"""

class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        for i in range(1,len(triangle)):
            for j in range(len(triangle[i])):
                t = min(triangle[i-1][j-1] if j!=0 else float("inf"),triangle[i-1][j] if len(triangle[i-1])>j else float("inf"))
                triangle[i][j] += t
        return min(triangle[-1])



if __name__ == '__main__':
    solution = Solution()
    result = solution.minimumTotal([
        [2],
        [3,4],
        [6,5,7],
        [4,1,8,3]
    ])
    print(result)
