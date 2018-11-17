# -*- coding:utf-8 -*-
# __author__ = 'wanhaoran'

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        def find_kth(nums1, nums2, k):
            len1 = len(nums1)
            len2 = len(nums2)
            if k > len1 + len2:
                return None
            if len1 == 0:
                return nums2[k-1]
            if len2 == 0:
                return nums1[k-1]
            if k == 1:
                return min(nums1[0], nums2[0])
            # mid_index1, mid_index2 = k // 2 - 1, k // 2 - 1

            a = nums1[k//2-1] if len1 >k//2-1 else None
            b = nums2[k//2-1] if len2 >k//2-1 else None

            if a is None or (b is not None and a >b):
                return find_kth(nums1,nums2[k//2:],k-k//2)
            return find_kth(nums1[k//2:],nums2,k-k//2)

        len1 = len(nums1)
        len2 = len(nums2)
        k = (len1+len2)/2
        if not k.is_integer():
            return find_kth(nums1,nums2,int(k+1))
        else:
            return (find_kth(nums1,nums2,int(k))+find_kth(nums1,nums2,int(k+1)))/2

        # if len1 <= mid_index1:
        #     mid_index1, mid_index2 = len1 - 1, mid_index2 + mid_index1-len1+1
        # elif len2 <= mid_index2:
        #     mid_index1, mid_index2 = k + len2, len2 - 1
        # print("k=",k," mid_index1=",mid_index1," mid_index2=",mid_index2)
        # if nums1[mid_index1] < nums2[mid_index2]:
        #     return self.find_kth(nums1[mid_index1 + 1:], nums2, k - mid_index1-1)
        # if nums1[mid_index1] > nums2[mid_index2]:
        #     return self.find_kth(nums1, nums2[mid_index2 + 1:], k - mid_index2-1)

if __name__ == '__main__':
    nums1 = [3]
    nums2= [-2,-1]
    k=7
    # print(Solution().find_kth(nums1,nums2,k))
    print(Solution().findMedianSortedArrays(nums1,nums2))