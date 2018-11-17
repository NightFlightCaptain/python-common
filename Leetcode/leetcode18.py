# -*- coding:utf-8 -*-
# @Time      :2018/11/17 22:25
# @Author    :wanhaoran
# @FileName  :leetcode18.py

class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        length, res = len(nums), []
        nums.sort()
        print(nums)
        for i in range(length):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i+1, length):
                if j - i-1 > 0 and nums[j] == nums[j - 1]:
                    continue
                l, r = j + 1, length - 1
                while l < r:
                    tmp = nums[i] + nums[j] + nums[l] + nums[r]
                    if tmp == target:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                        print('r',r)
                        while l < r and nums[r] == nums[r + 1]:
                            r -= 1
                    elif tmp < target:
                        l += 1
                    else:
                        r -= 1
        return res


if __name__ == '__main__':
    print(Solution().fourSum([5,5,3,5,1,-5,1,-2],4))
