# -*- coding:utf-8 -*-
# @Time      :2018/11/17 21:44
# @Author    :wanhaoran
# @FileName  :leetcode16.py

class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        length,result = len(nums),nums[0]+nums[1]+nums[2]
        nums.sort()
        for i in range(length):
            if i>0 and nums[i]==nums[i-1]:
                continue
            l,r = i+1,length-1
            while l < r:
                tmp = nums[i]+nums[l]+nums[r]
                if tmp == target:
                    return target
                result = tmp if abs(target-tmp) < abs(target-result) else result
                if tmp <target:
                    l+=1
                else:
                    r-=1
        return result

if __name__ == '__main__':
    nums,target = [-1,2,1,-4],1
    print(Solution().threeSumClosest(nums,target))