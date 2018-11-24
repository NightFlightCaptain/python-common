# -*- coding:utf-8 -*-
# @Time      :2018/11/24 15:19
# @Author    :wanhaoran
# @FileName  :leetcode198.py


"""
你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。

示例 1:

输入: [1,2,3,1]
输出: 4
解释: 偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
     偷窃到的最高金额 = 1 + 3 = 4 。
示例 2:

输入: [2,7,9,3,1]
输出: 12
解释: 偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
     偷窃到的最高金额 = 2 + 9 + 1 = 12 。
"""

class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums)==0:
            return 0
        length = len(nums)
        max_n = [0]*(length+1)
        max_n[1] = nums[0]
        for i in range(2,length+1):
            max_n[i]=max(max_n[i-1],max_n[i-2]+nums[i-1])
        return max_n[-1]

if __name__ == '__main__':
    solution = Solution()
    result = solution.rob([1,2,3,1])
    print(result)