# -*- coding:utf-8 -*-
# @Time      :2018/12/13 10:36
# @Author    :wanhaoran
# @FileName  :leetcode300.py

"""
给定一个无序的整数数组，找到其中最长上升子序列的长度。

示例:

输入: [10,9,2,5,3,7,101,18]
输出: 4
解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
说明:

可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。
你算法的时间复杂度应该为 O(n2) 。
进阶: 你能将算法的时间复杂度降低到 O(n log n) 吗?
"""


class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        """
        O(n^2)
        """

        # if nums is None or len(nums)==0:
        #     return 0
        # dp = [0 for i in nums]
        # for i in range(1,len(nums)):
        #     for j in range(i):
        #         if nums[i] > nums[j]:
        #             dp[i] = dp[j]+1 if dp[j]+1>dp[i] else dp[i]
        # return max(dp)+1

        def binarySearch(nums, l, r, target):
            while l <= r:
                mid = l + (r - l) // 2
                if nums[mid] >= target:
                    r = mid - 1
                else:
                    l = mid + 1
            return l

        if nums is None or len(nums) == 0:
            return 0
        dp = [0 for i in range(len(nums) + 1)]
        dp[0] = nums[0]
        max_length = 1
        for i in range(1, len(nums)):
            if nums[i] < dp[0]:
                dp[0] = nums[i]
            elif nums[i] > dp[max_length-1]:
                dp[max_length] = nums[i]
                max_length += 1
            else:
                dp[binarySearch(dp,0,max_length-1,nums[i])] = nums[i]
        return max_length

if __name__ == '__main__':
    solution = Solution()
    result = solution.lengthOfLIS([1, 3, 6, 7, 9, 4, 10, 5, 6])
    print(result)
