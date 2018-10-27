# -*- coding:utf-8 -*-
# __author__ = 'wanhaoran'

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        m, n = len(nums1), len(nums2)
        if m >n :
            nums1,nums2,m,n = nums2,nums1,n,m
        if n == 0 :
            raise ValueError


