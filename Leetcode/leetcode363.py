# -*- coding:utf-8 -*-
# @Time      :2018/12/14 15:16
# @Author    :小栗旬
# @FileName  :leetcode363.py

"""
363. Max Sum of Rectangle No Larger Than K
Hard


Given a non-empty 2D matrix matrix and an integer k, find the max sum of a rectangle in the matrix such that its sum is no larger than k.

Example:

Input: matrix = [[1,0,1],[0,-2,3]], k = 2
Output: 2
Explanation: Because the sum of rectangle [[0, 1], [-2, 3]] is 2,
             and 2 is the max number no larger than k (k = 2).
Note:

The rectangle inside the matrix must have an area > 0.
What if the number of rows is much larger than the number of columns?
"""
import bisect
import sys

"""
Kadane's algorithm
"""


class Solution:
    def maxSumSubmatrix(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        """
        没有k限制的求解
        """
        # def find_max_list(nums):
        #     max_ending_here=max_so_far = nums[0]
        #     max_index_left, max_index_right = 0, 0
        #     next_left_position = 0
        #     for index in range(1, len(nums)):
        #
        #         max_ending_here += nums[index]
        #
        #         if max_ending_here>max_so_far:
        #             max_so_far = max_ending_here
        #             max_index_left = next_left_position
        #             max_index_right = index
        #
        #         if max_ending_here < 0:
        #             max_ending_here=0
        #             next_left_position = index+1
        #
        #     return max_so_far, max_index_left, max_index_right
        #
        #
        # # for nums in matrix:
        # #     print(find_max_list(nums))
        # # print(find_max_list([-4,-13,-3,-6,-5]))
        #
        # m = len(matrix)
        # n = len(matrix[0]) if m != 0 else 0
        # # max_left, max_right, max_up, max_down = 0, 0, 0, 0
        # max_sum, max_current = -sys.maxsize-1,-sys.maxsize-1
        # cul_list = [0 for _ in range(m)]
        # for l in range(0, n):
        #     for r in range(l, n):
        #         for i in range(m):
        #             cul_list[i] += matrix[i][r]
        #         max_current,up,down = find_max_list(cul_list)
        #         if max_current > max_sum :
        #             max_sum = max_current
        #             max_up = up
        #             max_down = down
        #             max_left,max_right = l,r
        #     cul_list = [0 for _ in range(m)]
        # return max_sum

        # for nums in matrix:
        #     print(find_max_list(nums))
        # print(find_max_list([-4,-13,-3,-6,-5]))

        M = len(matrix)
        N = len(matrix[0]) if M != 0 else 0

        m,n=max(M,N),min(M,N)
        ans = -sys.maxsize - 1
        for l in range(0, n):
            cul_list = [0 for _ in range(m)]
            for r in range(l, n):
                num = 0
                # slist中存储的是每一行累加的值
                slist = []
                for i in range(m):
                    cul_list[i] += matrix[i][r] if M>N else matrix[r][i]
                    num += cul_list[i]
                    if num == k:
                        return k
                    if num < k:
                        ans = max(ans, num)
                    # num-k表示的是当前num相较于k多了多少，这个多出的部分与list中的值比较，找出最接近的一个，减去之后就得到了
                    i = bisect.bisect_left(slist, num - k)
                    # 如果i==len(slist)表示num-k的值超过了所有slist的值,也就是用num-slist中的值时得到的结果会比k大
                    if i != len(slist):
                        ans = max(ans, num - slist[i])
                    # 将每一个sum存入slist
                    bisect.insort(slist, num)
        return ans


if __name__ == '__main__':
    solution = Solution()
    list = [[2, 1, -3, -4, 5],
            [-1, 6, 3, 4, 1],
            [2, -2, -1, 4, -5],
            [-3, 3, 1, -1, 3]]
    list2 = [[1],
             [2],
             [7],
             [10]]

    list3 =[[5,-4,-3,4],
            [-3,-4,4,5],
            [5,1,5,-4]]

    list4 = [[1,0,1],
             [0,-2,3]]
    result = solution.maxSumSubmatrix(list4, 2)
    print(result)

    # list = [1, 8, 9]
    # bisect.insort(list, 9)
    # print(list)
    # print(bisect.bisect_right(list, 6))
