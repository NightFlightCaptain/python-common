# -*- coding:utf-8 -*-
# @Time      :2018/12/13 15:42
# @Author    :wanhaoran
# @FileName  :leetcode321.py


"""
给定长度分别为 m 和 n 的两个数组，其元素由 0-9 构成，表示两个自然数各位上的数字。现在从这两个数组中选出 k (k <= m + n) 个数字拼接成一个新的数，要求从同一个数组中取出的数字保持其在原数组中的相对顺序。

求满足该条件的最大数。结果返回一个表示该最大数的长度为 k 的数组。

说明: 请尽可能地优化你算法的时间和空间复杂度。

示例 1:

输入:
nums1 = [3, 4, 6, 5]
nums2 = [9, 1, 2, 5, 8, 3]
k = 5
输出:
[9, 8, 6, 5, 3]
示例 2:

输入:
nums1 = [6, 7]
nums2 = [6, 0, 4]
k = 5
输出:
[6, 7, 6, 0, 4]
示例 3:

输入:
nums1 = [3, 9]
nums2 = [8, 9]
k = 3
输出:
[9, 8, 9]
"""


class Solution:
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """

        def find_max_num_list(nums, p):
            if p >= len(nums):
                return nums
            res = []
            drop = len(nums) - p
            for num in nums:
                while drop and res and res[-1] < num:
                    res.pop()
                    drop-=1
                res.append(num)
            return res[:p]

        def greater(nums1, i, nums2, j):
            while i < len(nums1) and j < len(nums2) and nums1[i] == nums2[j]:
                i += 1
                j += 1
            return j == len(nums2) or (i < len(nums1) and nums1[i] > nums2[j])

        length1 = len(nums1)
        length2 = len(nums2)
        result = []
        for count in range(k + 1):
            if count > length1 or k - count > length2:
                continue
            res = []
            i, j = 0, 0
            max_num1, max_num2 = find_max_num_list(nums1, count), find_max_num_list(nums2, k - count)
            while True:
                if i >= count:
                    res.extend(max_num2[j:])
                    break
                elif j >= k - count:
                    res.extend(max_num1[i:])
                    break

                if greater(max_num1, i, max_num2, j):
                    res.append(max_num1[i])
                    i += 1
                else:
                    res.append(max_num2[j])
                    j += 1

            if greater(res, 0, result, 0):
                result = res

        return result


if __name__ == '__main__':
    nums1 = [3, 8, 5, 3, 4]
    nums2 = [8, 7, 3, 6, 8]
    k = 5
    solution = Solution()
    result = solution.maxNumber(nums1, nums2, k)
    print(result)
