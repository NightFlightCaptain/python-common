# -*- coding:utf-8 -*-
# @Time      :2018/11/19 14:02
# @Author    :wanhaoran
# @FileName  :leetcode64.py


class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m,n = len(grid),len(grid[0])
        path = [[0 for i in range(n+1)] for j in range(m+1)]
        for i in range(1,m+1):
            path[i][1] = path[i-1][1]+grid[i-1][0]
        for i in range(1,n+1):
            path[1][i] = path[1][i-1]+grid[0][i-1]
        for i in range(2,m+1):
            for j in range(2,n+1):
                path[i][j] = min(path[i-1][j],path[i][j-1]) + grid[i-1][j-1]
        return path[m][n]


if __name__ == '__main__':
    print(Solution().minPathSum([
        [1,3,1],
        [1,5,1],
        [4,2,1]
    ]))