# -*- coding:utf-8 -*-
# @Time      :2018/12/18 11:06
# @Author    :小栗旬

"""
Given an integer array with all positive numbers and no duplicates, find the number of possible combinations that add up to a positive integer target.

Example:

nums = [1, 2, 3]
target = 4

The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

Note that different sequences are counted as different combinations.

Therefore the output is 7.
Follow up:
What if negative numbers are allowed in the given array?
How does it change the problem?
What limitation we need to add to the question to allow negative numbers?

Credits:
Special thanks to @pbrother for adding this problem and creating all test cases.
"""


class Solution:
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # if target == 0:
        #     return 1
        # res = 0
        # for num in nums:
        #     if target >= num:
        #         res += self.combinationSum4(nums,target-num)
        # return res

        dp = [0] * (target + 1)
        dp[0] = 1
        for j in range(target + 1):
            for num in nums:
                if j >= num:
                    dp[j] += dp[j - num]
        return dp[-1]


if __name__ == '__main__':
    solution = Solution()
    result = solution.combinationSum4([1, 2], 4)
    print(result)
