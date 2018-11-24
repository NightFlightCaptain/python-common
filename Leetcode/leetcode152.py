# -*- coding:utf-8 -*-
# @Time      :2018/11/24 19:43
# @Author    :wanhaoran
# @FileName  :leetcode152.py


"""
给定一个整数数组 nums ，找出一个序列中乘积最大的连续子序列（该序列至少包含一个数）。

示例 1:

输入: [2,3,-2,4]
输出: 6
解释: 子数组 [2,3] 有最大乘积 6。
示例 2:

输入: [-2,0,-1]
输出: 0
解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。
"""


class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums)==0:
            return 0
        maxdp,mindp=[nums[0]],[nums[0]]
        for i in nums[1:]:
            maxdp.append(max(maxdp[-1]*i,mindp[-1]*i,i))
            mindp.append(min(maxdp[-2]*i,mindp[-1]*i,i))
        return max(maxdp)

if __name__ == '__main__':
    solution = Solution()
    result = solution.maxProduct([-4,-3,-2])
    print(result)