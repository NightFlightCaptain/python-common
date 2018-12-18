# -*- coding:utf-8 -*-
# @Time      :2018/12/18 9:48
# @Author    :小栗旬

"""
Given a set of distinct positive integers, find the largest subset such that every pair (Si, Sj) of elements in this subset satisfies:

Si % Sj = 0 or Sj % Si = 0.

If there are multiple solutions, return any subset is fine.

Example 1:

Input: [1,2,3]
Output: [1,2] (of course, [1,3] will also be ok)

Example 2:

Input: [1,2,4,8]
Output: [1,2,4,8]
"""


class Solution:
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        """
        another solution
        """
        # S的key为nums中的值，value为其能够整除的数的集合
        S = {-1: set()}
        for x in sorted(nums):
            S[x] = max((S[d] for d in S if x % d == 0), key=len) | {x}
        return list(max(S.values(), key=len))

        # nums.sort()
        # length = len(nums)
        #
        # res = []
        #
        # pre = [-1] * length
        # count = [0] * length
        #
        # max_count = 0
        # index = -1
        # for i in range(length):
        #     count[i] = 1
        #     for j in range(i - 1, -1, -1):
        #         if nums[i] % nums[j] == 0:
        #             if count[j] + 1 > count[i]:
        #                 count[i] = count[j] + 1
        #                 pre[i] = j
        #     if count[i] > max_count:
        #         max_count = count[i]
        #         index = i
        #
        # while index != -1:
        #     res.append(nums[index])
        #     index = pre[index]
        # return res


if __name__ == '__main__':
    solution = Solution()
    result = solution.largestDivisibleSubset([1, 3, 9, 18, 54, 90, 108, 180, 360, 540, 720])
    print(result)
